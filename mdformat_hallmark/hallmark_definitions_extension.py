from contextlib import suppress
from dataclasses import dataclass
import re

from markdown_it import MarkdownIt
from markdown_it.token import Token
from mdformat.plugins import ParserExtensionInterface
from mdformat.renderer import RenderContext, RenderTreeNode
from packaging.version import InvalidVersion, Version

_DEFINITION_RE = re.compile(
    r'^\[([^\]]+)\]:\s*(\S+)(?:\s+"([^"]+)")?$',
    re.MULTILINE,
)  # regex for `[label]: href "title"`


@dataclass
class SemverDefinition:
    semver: Version
    label: str
    href: str
    title: str | None


@dataclass
class Definition:
    label: str
    href: str
    title: str | None


def _extract_references(src: str, is_changelog: bool) -> tuple[list[Definition], str]:
    semver_defs: list[SemverDefinition] = []
    remark_defs: list[Definition] = []
    remove_spans: list[tuple[int, int]] = []

    for m in _DEFINITION_RE.finditer(src):
        label, href, title = m.groups()
        semver = None
        if is_changelog:
            with suppress(InvalidVersion):
                semver = Version(label)
                semver_defs.append(SemverDefinition(semver, label, href, title))
        if not semver:
            # remove definition has no references
            reference_re = rf"\[{re.escape(label)}\](?!:)"
            if re.search(reference_re, src, flags=re.MULTILINE):
                remark_defs.append(Definition(label, href, title))
        remove_spans.append(m.span())

    # remove references from the source
    out_src = src
    for start, end in reversed(remove_spans):
        out_src = out_src[:start] + out_src[end:]

    # Normalize whitespace
    out_src = re.sub(r"\n{3,}", "\n\n", out_src).rstrip()

    # sort semver references
    semver_defs.sort(key=lambda ref: ref.semver, reverse=True)

    # sort remark references
    remark_defs.sort(key=lambda ref: ref.label)

    out_refs = [Definition(ref.label, ref.href, title) for ref in semver_defs]
    out_refs.extend(remark_defs)
    return out_refs, out_src


class HallmarkDefinitionsExtension(ParserExtensionInterface):
    """mdformat plugin extension to format definitions in remark and hallmark style.

    * Hallmark detected Changelog versions used as definition labels are
      rendered first by descending semantic-version order.
    * Remark detected definitions are rendered after by alphanumeric order.
    * All definition labels keep the original casing.
    """

    @staticmethod
    def update_mdit(mdit: MarkdownIt) -> None:
        """Patch the default parser to render references in semver order."""

        original_parse = mdit.parse

        def new_parse(src: str, env=None):
            if env is None:
                env = {}

            is_changelog = src.lstrip().startswith("# Changelog")

            # extract definitions and remove from src
            remark_defs, out_src = _extract_references(src, is_changelog)
            defs = {
                match.label: {"href": match.href, "title": match.title}
                for match in remark_defs
            }

            # call original parse on the cleaned text
            tokens = original_parse(out_src, env)

            # append a remark_defs token at the end
            if defs:
                token = Token("remark_defs", "", 0)
                token.meta = {"refs": defs}
                tokens.append(token)

            return tokens

        # patch parser
        mdit.parse = new_parse

    @staticmethod
    def _render_remark_defs(node: RenderTreeNode, ctx: RenderContext) -> str:
        """Render collected reference defs in hallmark ordered format."""
        refs: dict[str, dict[str, str]] = node.meta["refs"]
        out = []
        for label, ref in refs.items():
            line = f"[{label}]: {ref['href']}"
            if ref.get("title"):
                line += f' "{ref["title"]}"'
            out.append(line)
        return "\n\n".join(out)

    RENDERERS = {"remark_defs": _render_remark_defs}
    CHANGES_AST = True
