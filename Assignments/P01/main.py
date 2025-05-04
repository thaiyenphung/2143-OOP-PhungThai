import os
import sys
from nobelDB import NobelDB
from rich import print

# Get current directory of main.py
current_dir = os.path.dirname(os.path.abspath(__file__))

# Path to the JSON file
json_path = os.path.join(current_dir, "nobel_db.json")

# Check if the JSON file exists
if not os.path.exists(json_path):
    print(f"ERROR: File not found: {json_path}")
    print("Please make sure 'nobel_db.json' is in the same folder as this file.")
    sys.exit(1)

# Create database object
db = NobelDB(json_path)

# Display search menu
print("Nobel Prize Database")
print("Search for laureate(s) by:")
print("- id")
print("- year")
print("- category")
print("- firstname")
print("- surname")
print("- motivation")
print()

# Ask user for search type
searchType = input("Enter search type (e.g. category): ").strip().lower()

# Ask for the search value
if searchType == "id":
    value = input("Enter ID to search: ").strip()
    results = db.search_laureates(id=value)

elif searchType == "year":
    value = input("Enter year to search: ").strip()
    results = db.search_laureates(year=value)

elif searchType == "category":
    value = input("Enter category to search: ").strip()
    results = db.search_laureates(category=value)

elif searchType == "firstname":
    value = input("Enter firstname to search: ").strip()
    results = db.search_laureates(firstname=value)

elif searchType == "surname":
    value = input("Enter surname to search: ").strip()
    results = db.search_laureates(surname=value)

elif searchType == "motivation":
    value = input("Enter keyword in motivation to search: ").strip()
    results = db.search_laureates(motivation=value)

else:
    print("Invalid search type. Please run the program again.")
    sys.exit(1)

# Show search results
print()
if results:
    print(f"Found {len(results)} result(s):")
    for r in results:
        print(r)
else:
    print("No matches found.")