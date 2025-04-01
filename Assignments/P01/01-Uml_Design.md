![image](https://github.com/user-attachments/assets/0ffa80fc-c632-4b81-b473-1148106744ba)

### Description:
#### `ProductManager` class
- This class controls the entire `skincare product inventory system`
- Calls methods from JSONDBManager to load, save, and manage product data stored in a JSON file
- Handles the main operations that allow users to create, read, update, and delete skincare items (CRUD)
- Handles error checking by validating input values and checking for duplicate or missing IDs
- Has a **composition** relationship with `SKProduct` class:
  - It controls the lifecycle of each skincare product object
  - When `ProductManager` is destroyed, all `SKProduct` objects are also destroyed.

#### `SKProduct` class
- This class represents a single skincare product with its properties and behaviors
- Focuses only on storing product data, not performing file operations or program logic
- Has private attributes like `id`, `name`, `price`, `category` (e.g., cleanser, toner, serum), and `skinType` (e.g., dry, oily, combination) 
- Provides getter and setter methods for each attribute
- `toJSON()` method to convert a skincare product object to JSON
- `createFromJSON(`) to build a skincare product from JSON data

#### `JSONDBManager` class
- This class handles reading from and writing to from a JSON file
- Converts between JSON format and `SKProduct` object
- Handles file errors
- `readFromFile()` and `saveData()` for file access 
- `addItem()`, `getItem()`, `updateItem()`, and `deleteItem()` for CRUD operations
- Has an aggregation relationship with `ProductManager`:
  - `ProductManager` has access to a `JSONDBManager` object and uses its methods
  - However, it does not control its lifecycle (it doesn't create or delete it)
 
   
