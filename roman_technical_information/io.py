def open_data(relative_path: str):
    """Return a file handle for a data file inside roman_technical_information/data."""
    return (PACKAGEDIR / relative_path).open("r")

def load_yaml(relative_path: str):
    with open_data(PACKAGEDIR / relative_path) as f:
        return yaml.safe_load(f)

def load_table(relative_path: str) -> Table:
    path = PACKAGEDIR / relative_path
    return Table.read(path, format="ascii.ecsv")