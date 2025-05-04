# P01 – Nobel Prize JSON Project

This project is part of a class assignment to help us practice working with JSON files and build a basic CRUD (Create, Read, Update, Delete) system using Python.

---

## What’s This Project About?

We’re using a real Nobel Prize dataset stored in a `.json` file. The goal is to create a program that can:

- Search for laureates by year, name, category, ID, or motivation
- Add new laureates to the database
- Update motivation for a laureate
- Delete a laureate by ID

We also built a **terminal menu** using `InquirerPy` so it’s interactive and beginner-friendly!

---

## What’s Inside?

- `nobel_db.py`: Base class that handles the JSON file and all CRUD operations
- `menu.py` & `main.py`: The main file that runs the menu and connects everything
- `nobel_db.json`: The actual dataset (not modified directly)
- `myKwargs.py` & `params.py`: Optional helper files for command-line features

