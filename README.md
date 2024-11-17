To-Do Application
=================

This is a simple **To-Do Application** built with Python and Tkinter. It uses the MVC (Model-View-Controller) architecture for modularity and maintains task persistence using JSON file storage.

Features
--------
- Add and delete tasks via a simple GUI.
- Persist tasks across sessions using a JSON file.
- Modular design for easy extension and maintenance.

Project Structure
-----------------
todo_app/
├── app.py                # Entry point
├── models/
│   ├── __init__.py       # Models package
│   ├── todo_model.py     # Task management logic
├── views/
│   ├── __init__.py       # Views package
│   ├── main_view.py      # GUI implementation
├── controllers/
│   ├── __init__.py       # Controllers package
│   ├── todo_controller.py  # Intermediary between model and view
└── utils/
    ├── __init__.py       # Utils package
    ├── file_handler.py   # Handles JSON file storage

How to Run
----------
1. Clone the project or create the folder structure manually.
2. Install Python (if not already installed).
3. Navigate to the project directory:
   cd path/to/todo_app
4. Run the application:
   python app.py

Dependencies
------------
- Python 3.x: Ensure Python is installed on your system.
- Tkinter: Included by default in Python.

Future Enhancements
-------------------
- Add features like task editing or due dates.
- Improve GUI with more advanced widgets.
- Add search functionality for tasks.

Author
------
Created by [Sabona Waktole].
