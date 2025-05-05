import json
from rich import print

class JsonDB:
    """
    Base class for a simple JSON "database."

    Attributes:
        filepath (str): Path to the JSON file on disk.
        data (any): The loaded JSON data (e.g., list, dict).
    """
    def __init__(self, filepath):
        """
        Initialize the DB with a path to the JSON file.
        """
        self.filepath = filepath
        self.data = None
        self._load_data()
        self.current = 0

    def _load_data(self):
        """
        Internal helper to load JSON data from the file into self.data.
        Handle exceptions and set self.data appropriately if file is missing/corrupted.
        """
        with open(self.filepath) as f:
            self.data = json.load(f)

    def _save_data(self):
        """
        Internal helper to save self.data back to the JSON file.
        """
        with open(self.filepath, 'w') as f: # 'w' is write mode
            json.dump(self.data, f, indent=4)

    