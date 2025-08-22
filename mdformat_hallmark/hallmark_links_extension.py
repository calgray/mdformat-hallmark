from markdown_it import MarkdownIt
from mdformat.renderer import RenderTreeNode, RenderContext
from mdformat.plugins import ParserExtensionInterface
from markdown_it.token import Token
import re


class HallmarkLinksExtension(ParserExtensionInterface):
    """
    mdformat plugin extension to format references used by versions and 
    renders sorted by semantic-version order.
    """
    @staticmethod
    def update_mdit(mdit: MarkdownIt) -> None:
        # save original parser
        original_parse = mdit.parse

        def new_parse(src: str, env=None):
            if env is None:
                env = {}

            # regex for `[label]: href "title"`
            pattern = re.compile(
                r'^\[([^\]]+)\]:\s*(\S+)(?:\s+"([^"]+)")?$',
                re.MULTILINE,
            )

            # collect defs
            matches = pattern.findall(src)
            refs = {
                label: {"href": href, "title": title}
                for label, href, title in matches
            }

            # remove them from the source
            src = pattern.sub("", src).rstrip()

            # call original parse on the cleaned text
            tokens = original_parse(src, env)

            # append a dummy hallmark_refs token at the end
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
        sorted_ref_items = reversed(list(refs.items()))
        for label, ref in sorted_ref_items:
            line = f"[{label}]: {ref['href']}"
            if ref.get("title"):
                line += f' "{ref["title"]}"'
            out.append(line)
        return "\n".join(out) + "\n"

    RENDERERS = {"hallmark_refs": _render_hallmark_refs}
    CHANGES_AST = True
