#!/usr/bin/python

# simple-walk-demo.py

import os

for dirpath, dirnames, filenames in os.walk("C:\\opt\\hector2018\\Programming\\python\\code\PyRefCodeNotes\\"):
    print("Files in %s are:" % dirpath)
    for file in filenames:
        print("\t" + file)
    print("Directories in %s are:" % dirpath)
    for dir in dirnames:
        print("\t" + dir)
        
