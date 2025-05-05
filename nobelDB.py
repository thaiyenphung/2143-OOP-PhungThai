from json_db import JsonDB
from rich import print

class NobelDB(JsonDB):
    """
    NobelDB is a subclass that extends JsonDB to work with 
    the nobel prize database.
    """
    def __init__(self, filepath):
        """
        Initialize the NobelDB class with a path to the JSON file.
        """
        super().__init__(filepath)
        self.current = 0
        self._load_data()
        self._save_data()
        
    def get_prize_by_year(self, year):
        """
        Get the prize data for a specific year.
        """
        # empty list to store the matchingn prizes
        result = [] 
        # loop through the data and check if the year matches
        for prize in self.data:
            # check if the prize year is equal to the given year
            if prize['year'] == year:
                # add the prize to the result list
                result.append(prize)
        return result

    def add_laureate(self, year, category, laureate):
        """
        Add a new laureate to the database.
        """
        # loop through the prizes and check if the year and category match
        for prize in self.data["prizes"]:
            if prize["year"] == year and prize["category"] == category:
                # found the right prize entry, add the laureate to the laureates list
                prize["laureates"].append(laureate)
                self._save_data()
                return True
            
        # if not found, create a new prize entry
        new_prize = {
            "year": year,
            "category": category,
            "laureates": [laureate]
        }
        self.data["prizes"].append(new_prize)
        self._save_data()
        return True
    
    def search_laureates(self, **filter):
        """
        Search for laureates based on the provided filter criteria.
        """
        year = filter.get("year")
        category = filter.get("category")
        firstname = filter.get("firstname")
        surname = filter.get("surname")
        id = filter.get("id")
        motivation = filter.get("motivation")
        
        results = []
        
        for prize in self.data["prizes"]:
            prize_matches = True

            if year and prize.get("year") != year:
                prize_matches = False
            if category and prize.get("category") != category:
                prize_matches = False

            if prize_matches:
                for laureate in prize.get("laureates", []):
                    match = True

                    if firstname and laureate.get("firstname", "").lower() != firstname.lower():
                        match = False
                    if surname and laureate.get("surname", "").lower() != surname.lower():
                        match = False
                    if id and laureate.get("id") != id:
                        match = False
                    if motivation and motivation.lower() not in laureate.get("motivation", "").lower():
                        match = False

                    if match:
                        results.append({
                            "year": prize["year"],
                            "category": prize["category"],
                            "laureate": laureate
                        })

        return results
        
        
    def update_motivation(self, id, new_motivation):
        """
        Update the motivation for a laureate by their ID.
        """
        for prize in self.data["prizes"]:
            for laureate in prize["laureates"]:
                if laureate["id"] == id:
                    laureate["motivation"] = new_motivation
                    self._save_data()
                    return True
        return False
    
    
    def delete_laureate(self, id):
        """
        Delete a laureate from the database by their ID.
        Searches each prize entry and removes the matching laureate using remove()
        """
        for prize in self.data["prizes"]:
            for laureate in prize["laureates"]:
                if laureate["id"] == id:
                    prize["laureates"].remove(laureate)
                    self._save_data()
                    return True
        # if no match was found
        return False