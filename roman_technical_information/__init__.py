from pathlib import Path
from importlib.resources import files
import yaml
from astropy.table import Table, QTable


_version_file = Path(__file__).parent.parent / "VERSION.md"
__version__ = _version_file.read_text(encoding="utf-8").strip()

PACKAGEDIR = files("roman_technical_information") / "data"