from nobelDB import NobelDB
from rich import print  
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

json_path = os.path.join(current_dir, "nobel_db.json")

# Confirm the file exists (optional, for debugging)
if not os.path.exists(json_path):
    print(f"[ERROR] File not found: {json_path}")
else:
    print(f"[INFO] Loaded JSON file from: {json_path}")
       
if __name__ == "__main__":
    # create a JsonDB object using your JSON file
    db = NobelDB(json_path)

    # search for laureates with specific filters
    data = db.search_laureates(
        year="2020",
        category="economics",
        firstname="Robert"
    )

    # Print the search results
    print(data)