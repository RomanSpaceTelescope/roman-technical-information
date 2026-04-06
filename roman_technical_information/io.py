from importlib.resources import files
import yaml
from astropy.table import Table, QTable

BASE = files("roman_technical_information") / "data"

def open_data(relative_path: str):
    """Return a file handle for a data file inside roman_technical_information/data."""
    return (BASE / relative_path).open("r")

def load_yaml(relative_path: str):
    with open_data(relative_path) as f:
        return yaml.safe_load(f)

def load_table(relative_path: str, table_class=Table):
    path = BASE / relative_path
    return table_class.read(path, format="ascii.ecsv")