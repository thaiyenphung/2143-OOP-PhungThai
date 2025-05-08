# P01 – Nobel Prize JSON Project

| File Name           | Description                                           | Link                              |
|--------------------|-------------------------------------------------------|------------------------------------|
| `README.md`        | Project documentation                                 | [README.md](./README.md)           |
| `nobel_db.json`    | Nobel Prize dataset in JSON format                    | [nobel_db.py](./nobel_db.json) |
| `json_db.py`       | Base class for handling JSON database functionality   | [json_db](./json_db.py)        |
| `nobelDB.py`       | NobelDB subclass for managing Nobel Prize data        | [nobelDB.py](./nobelDB.py)     |
| `main.py`          | Simple starter script for performing searches         | [main.py](./main.py)           |
| `menu.py`          | Terminal UI using InquirerPy for CRUD operations      | [menu.py](./menu.py)           |
| `myKwargs.py`      | Utility for parsing keyword arguments from terminal   | [myKwargs.py](./myKwargs.py)   |
| `params.py`        | Optional parameters file used in command-line setups  | [params.py](./params.py)       |

---

## What’s This Project About?

I'm using a real Nobel Prize dataset stored in a `.json` file. The goal is to create a program that can:

- Search for laureates by year, name, category, ID, or motivation
- Add new laureates to the database
- Update motivation for a laureate
- Delete a laureate by ID

The project also includes an interactive **terminal menu** built with `InquirerPy`, so it's user-friendly and easy to navigate.

---

## What’s Inside?

- `nobel_db.py`: Base class that handles the JSON file and all CRUD operations
- `menu.py` & `main.py`: The main file that runs the menu and connects everything
- `nobel_db.json`: The actual dataset
- `myKwargs.py` & `params.py`: Optional helper files for command-line features
