from nobelDB import NobelDB
from rich import print      
       
if __name__ == "__main__":
    # create a JsonDB object using your JSON file
    db = NobelDB("nobel_db.json")

    # search for laureates with specific filters
    data = db.search_laureates(
        year="2020",
        category="economics",
        firstname="Robert"
    )

    # Print the search results
    print(data)