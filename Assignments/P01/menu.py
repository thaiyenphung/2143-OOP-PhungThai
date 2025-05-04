from InquirerPy import inquirer
from rich import print
from nobelDB import NobelDB
from rich.console import Console

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Load the JSON data dynamically
current_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.normpath(os.path.join(current_dir, "..", "JSON PROJECT", "nobel_db.json"))

if not os.path.exists(json_path):
    print(f"[red]ERROR: File not found: {json_path}[/red]")
    exit()
    
# db = NobelDB('/Users/thaiyenphung/Desktop/OOP_CMPS_Sp25/JSON Project/nobel_db.json')

db = NobelDB(json_path)
console = Console()

def submenuCreate():
    """
    Add a new laureate
    """
    year = console.input("[blue]Enter year: [/blue]")
    category = console.input("[blue]Enter category: [/blue]")
    id = console.input("[blue]Enter id: [/blue]")
    firstname = console.input("[blue]Enter firstname: [/blue]")
    surname = console.input("[blue]Enter surname: [/blue]")
    motivation = console.input("[blue]Enter motivation: [/blue]")
    share = console.input("[blue]Enter share: [/blue]")
    
    if db.add_laureate(year, category, {
        "id": id,
        "firstname": firstname,
        "surname": surname,
        "motivation": motivation,
        "share": share,
    }):
        print("[green]Laureate added successfully![/green]")
    else:
        print("[red]Failed to add laureate.[/red]")
        

def submenuSearch():
    # Ask the user what field they want to search by
    searchType = inquirer.select(
        message="Search Type",
        choices=["ID", "Year", "Category", "First Name", "Surname", "Motivation", "Back"]
    ).execute()

    if searchType == "Back":
        return

    # Ask the user to enter a search keyword
    keyword = console.input("[blue]Enter the {searchType.lower()} to search: [/blue] ")

    # Map the search type to the actual field name in the JSON
    field_map = {
        "ID": "id",
        "Year": "year",
        "Category": "category",
        "First Name": "firstname",
        "Surname": "surname",
        "Motivation": "motivation"
    }

    # Perform the search using keyword arguments
    result = db.search_laureates(**{field_map[searchType]: keyword})

    # Show results
    print(f"[green]Searching for {searchType.lower()} = '{keyword}'... Done![/green]")
    
    if result:
        print("[green]Search complete. Results:[/green]")
        for item in result:
            print(item)
    else:
        print("[yellow]No matches found.[/yellow]")
    # Return to the same submenu
    submenuSearch()
    
    
def submenuUpdate():
    """
    Update laureate motivation
    """
    id = console.input("[blue] Enter laureate ID to update: [/blue]")
    new_motivation = console.input("[blue] Enter new motivation: [/blue]")
    
    if db.update_laureate_motivation(id, new_motivation):
        print("[green]Laureate motivation updated successfully![/green]")
    else:
        print("[red]No laureate found with that ID.[/red]")
    

def submenuDelete():
    id = console.input("[blue] Enter laureate ID to delete: [/blue]")

    if not id.isdigit():
        print("[red]Invalid ID. Try again.[/red]")
        return
    
    if db.delete_laureate(id):
        print("[green]Laureate deleted successfully![/green]")
    else:
        print("[red]Failed to delete laureate.[/red]")
        
        
def main_menu():
    """
    Main menu with CRUD options
    """
    while True:
        choice = inquirer.select(
            message="Nobel Prize Database - Select an option:",
            choices=["Create", "Search", "Update", "Delete", "Exit"],
        ).execute()

        if choice == "Create":
            submenuCreate()
        elif choice == "Search":
            submenuSearch()
        elif choice == "Update":
            submenuUpdate()
        elif choice == "Delete":
            submenuDelete()
        elif choice == "Exit":
            print("[bold red]Goodbye![/bold red]")
            break


if __name__ == "__main__":
    main_menu()