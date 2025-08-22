"""An mdformat plugin for compatibility with hallmark formatted Markdown and Common-Changelog."""

__version__ = "0.0.1"

from .hallmark_links_extension import HallmarkLinksExtension


__all__ = [
    "HallmarkLinksExtension"
]