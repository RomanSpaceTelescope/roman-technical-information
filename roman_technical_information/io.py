from importlib.resources import as_file, files
from astropy.table import Table
import yaml

from . import PACKAGEDIR


def open_data(relative_path: str):
    """Return a file handle for a data file inside roman_technical_information/data."""
    return (PACKAGEDIR / relative_path).open("r")


def load_yaml(relative_path: str):
    """Load a YAML file located under the package data directory."""
    with open_data(relative_path) as f:
        return yaml.safe_load(f)


def load_table(relative_path: str) -> Table:
    """Load an ECSV table located under the package data directory."""
    path = PACKAGEDIR / relative_path
    return Table.read(path, format="ascii.ecsv")