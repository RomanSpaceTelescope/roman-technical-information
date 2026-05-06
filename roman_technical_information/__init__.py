from pathlib import Path

_version_file = Path(__file__).parent.parent / "VERSION.md"
__version__ = _version_file.read_text(encoding="utf-8").strip()