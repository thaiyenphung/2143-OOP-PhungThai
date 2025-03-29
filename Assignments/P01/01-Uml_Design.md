![image](https://github.com/user-attachments/assets/6cfaf9aa-d31e-4e48-be26-7d36045de520)

### Description:
#### `CandyManager` class
- This class controls the entire candy inventory system
- Calls methods from JSONDBManager to load, save, and manage candy data stored in a JSON file
- Handles the main operations that allow users to create, read, update, and delete candy items (CRUD)
- Handles error checking by validating input values and checking for duplicate or missing IDs
- Has a **composition** relationship with `Candy` class:
  - It controls the lifecycle of each candy object
  - When `CandyManager` is destroyed, all `Candy` objects are also destroyed.

#### `Candy` class
- This class represents a single candy with its properties and behaviors
- Focuses only on storing the data, not performing file operations or program logic
- Has private attributes like `id`, `price`, `category`, `name`, `imageFormat`
- Provides getter and setter methods for each attribute
- `toJSON()` method to convert a candy object to JSON
- `createFromJSON(`) to build a candy from JSON data

#### `JSONDBManager` class
- This class handles reading from and writing to from a JSON file
- Converts between JSON format and `Candy` object
- Handles file errors
- `readFromFile()` and `saveData()` for file access 
- `addItem()`, `getItem()`, `updateItem()`, and `deleteItem()` for CRUD operations
- Has an aggregation relationship with `CandyManager`:
  - `CandyManager` has access to a `JSONDBManager` object and uses its methods
  - However, it does not control its lifecycle (it doesn't create or delete it)
 
   
