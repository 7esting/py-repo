"""
Docstring

project_root/
│
├── project/  # Project source code
├── docs/ # Documentation of the project
├── README  # Brief summery of project and DevOps requirements.
├── data # I/O Files
├── db # Database source code
├── <CUSTOM_PACKAGE_NAME>/  # User defined classes and functions OR modules
├── CONFIG_SETTINGS/  # JSON, or settings.py file for db connection string, etc.
├── examples.py # Script that gives simple examples of how to use the project.

IMPORTING MODULES:
project_root/
└── Game/ # Package
    ├── __init__.py
    └── Level/ # Package
        ├── __init__.py
        ├── load.py # Module
        ├── over.py # Module
        └── start.py # Module


# from <dir.file = package.module> import <class_name | method (case sensitive)>
# Pythonic: Yes
import Game  # dir(Game)
# Pythonic: No
from Game import *
# Pythonic: Yes
import Game.Level.start
from Game.Level.start import select_difficulty # help(select_difficulty)
import Game.Level.over
# Pythonic: No
import Game.Level.start, Game.Level.load
# Pythonic: Yes
from Game.Level import start, over # help(start)

"""
# ----------- Import Packages, and/or Modules: Classes, & Functions -----------


# --------------------------- Function Definitions ---------------------------


# ------------------------------- Main Function -------------------------------

## Main
# All functions are called in main.
# inputs: none
# returns: none
def main():
    pass

# ------------------------ Main Application Entry Point -----------------------
if __name__ == '__main__':
    main()
