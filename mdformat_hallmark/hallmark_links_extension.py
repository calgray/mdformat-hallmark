from dataclasses import dataclass
import re

from markdown_it import MarkdownIt
from markdown_it.token import Token
from mdformat.plugins import ParserExtensionInterface
from mdformat.renderer import RenderContext, RenderTreeNode
from packaging.version import InvalidVersion, Version

_REFERENCES_RE = re.compile(
    r'^\[([^\]]+)\]:\s*(\S+)(?:\s+"([^"]+)")?$',
    re.MULTILINE,
)  # regex for `[label]: href "title"`


@dataclass
class SemverReference:
    semver: Version
    label: str
    href: str
    title: str | None

    def __str__(self):
        line = f"[{self.label}]: {self.href}"
        if self.title:
            line += f' "{self.title}"'
        return line


def _extract_semver_references(src: str) -> tuple[list[SemverReference], str]:
    refs: list[SemverReference] = []
    remove_spans: list[tuple[int, int]] = []

    for m in _REFERENCES_RE.finditer(src):
        label, href, title = m.groups()
        try:
            semver = Version(label)
        except InvalidVersion:
            continue  # skip non-semver labels
        refs.append(SemverReference(semver, label, href, title))
        remove_spans.append(m.span())

    # remove references from the source
    out_src = src
    for start, end in reversed(remove_spans):
        out_src = out_src[:start] + out_src[end:]

    # Normalize whitespace
    out_src = re.sub(r"\n{3,}", "\n\n", out_src).rstrip()

    # sort semver references
    refs.sort(key=lambda ref: ref.semver, reverse=True)

    return refs, out_src


class HallmarkLinksExtension(ParserExtensionInterface):
    """
    mdformat plugin extension to format references used by versions and
    renders sorted by semantic-version order.
    """

    @staticmethod
    def update_mdit(mdit: MarkdownIt) -> None:
        """Patch the default parser to render references in semver order."""

        original_parse = mdit.parse

        def new_parse(src: str, env=None):
            if env is None:
                env = {}
            if not src.lstrip().startswith("# Changelog"):
                return original_parse(src, env)

            # extract semver references and remove from src
            matches, out_src = _extract_semver_references(src)
            refs = {
                match.label: {"href": match.href, "title": match.title}
                for match in matches
            }

            # call original parse on the cleaned text
            tokens = original_parse(out_src, env)

            # append a hallmark_refs token at the end
            if refs:
                token = Token("hallmark_refs", "", 0)
                token.meta = {"refs": refs}
                tokens.append(token)

            return tokens

        # patch parser
        mdit.parse = new_parse

    @staticmethod
    def _render_hallmark_refs(node: RenderTreeNode, ctx: RenderContext) -> str:
        """Render collected reference defs in hallmark ordered format."""
        refs: dict[str, dict[str, str]] = node.meta["refs"]
        out = []
        for label, ref in refs.items():
            line = f"[{label}]: {ref['href']}"
            if ref.get("title"):
                line += f' "{ref["title"]}"'
            out.append(line)
        return "\n".join(out)

    RENDERERS = {"hallmark_refs": _render_hallmark_refs}
    CHANGES_AST = True
