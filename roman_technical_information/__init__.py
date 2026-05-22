from pathlib import Path
from importlib.resources import files
import importlib.metadata
import yaml
from astropy.table import Table, QTable

try:
    # This reads the version directly from the pip metadata created by pyproject.toml
    __version__ = importlib.metadata.version("roman-technical-information")
except importlib.metadata.PackageNotFoundError:
    # Fallback if someone runs the code without installing it
    __version__ = "unknown"

PACKAGEDIR = files("roman_technical_information") / "data"