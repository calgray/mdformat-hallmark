"""
An mdformat plugin for compatibility with hallmark formatted Markdown
and Common Changelog.
"""

__version__ = "0.0.1"

from .hallmark_definitions_extension import HallmarkDefinitionsExtension

__all__ = ["HallmarkDefinitionsExtension"]
