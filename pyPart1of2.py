#!/usr/bin/env PyRefCodeNotes
"""
This is a docstring to describe the purpose of program.  The program can be
used as a reference to Python syntax.
"""
# -----------------------------------------------------------------------------
__author__ = "Socratica, Udemy, and myself"
__copyright__ = "Copyright 2018, Learning Python Project"
__credits__ = ["Socratica", "Udemy", "The Web",
                    "me"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Hector Maldonado"
__email__ = "7esting@gmail.com"
__status__ = "Dev"
# ---------------------------- Python3 -------------------------------
# URL  https://docs.python.org/3/tutorial/introduction.html
# Syntax and variables
# Operators: Arithmetic, Comparison (Relational), Assignment, Logical, Bitwise,
#   Membership (in, not in), Identity (is, is not)
# Decision/Control flow with IF-ELSE, and IF-ELIF-ELSE
# - URL https://docs.python.org/3/tutorial/controlflow.html
# - URL https://docs.python.org/3/tutorial/datastructures.html
# Loops: For-Loops, & While-Loops
# Functions
# Date & Time
# Fetching data from the internet & web scraping
# File I/O https://docs.python.org/3/tutorial/inputoutput.html
# Exceptions
# system calls, sockets, and interfaces to graphical user
# interface toolkits like Tk.
# Modules, packages, functions
# -----------------------------------------------------------------------------
"""
Abstract Data Type and Data Structures
- Classes

Primitive Data Structures
- Integers
- Float
- Strings
- Boolean

Non-Primitive Data Structures
- Lists/Arrays
  ~ List Comprehensions (a concise way to create lists)
- Tuples
- Dictionary
- Sets
- Files

Checking the type of an object or variable
type(varName)
type(objName)
"""

# ----------- Import Packages, and/or Modules: Classes, & Functions -----------
"""
Library : It is a collection of modules.
          (Library either contains built in modules(written in C) + modules written in
          python).

Module : Each of a set of standardized parts or independent units that can be used to
         construct a more complex structure.

Package is basically a directory with files.
"""
# from <dir.file = package.module> import <class_name | method (case sensitive)>
import math
from pprint import pprint
import random

# List available classes, and functions
print(dir(math))
# Help on sqrt function
help(math.sqrt)

# ---------------------------- Global Variables -------------------------------

print("\n--------------- Program Started! ---------------\n")

print("# ---------------------------- Numbers -------------------------------")
"""Python3 has three types of numbers: int, float, and complex."""
# Given a number to the power of one-half is that square root of that number
#  By the law of exponents Product Rule (X^a)(X^b)=X^(a+b)
#  Show that 4^0.5 = sqrt(4) => 2 
X = 2
Y = 4
a=0.5
b=0.5
z = 2 - 6.1j # Complex number
print(f"Type of number b=0.5: {type(b)}")
print(f"Complex number z=2-6.1j {type(z)}")
print(f"Real part of complex number: {z.real}")
print(f"Imaginary part of complex number: {z.imag}")
print("4^0.5 => %f" % Y**a)
print("2^(0.5+0.5) => %f" % X**(a+b))

print("# ---------------------------- Strings -------------------------------")
# Slicing strings
myName='hector'
print(myName[:3])
print(myName[0:3])
print(myName[3:])
capFirstLtrName = myName.capitalize()
print(capFirstLtrName)
x=myName.split('t')
# Doesn't include splitting character
print(x)
print(x[-1])
full_name = '{first_name} {last_name}'.format(first_name='Hector', last_name = 'Maldonado')
print(full_name)
# String concatination
wordOne="Basket"
wordTwo="ball"
print(wordOne + wordTwo)

print("# ---------------------------- Lists -------------------------------")
# Python Lists are synonymous to Arrays, which are mutable, and you
# can edit items, but not add new items, unless you re-define the
# list.
# Data Structure used for storing all data types:
#  int, float, string, etc
# Collections:
# - str
# - bytes
# - list
# - dict

# One-dimensional list  
siblings = ["Nico",42,"Hector",44]
siblings.append("Lupe")
siblings.append(46)
print(siblings)
siblings[5] = 'Mayo'
# At this poing the siblings list can accomodate 0-5 => 6 items
# assigning a 6th item will error, unless we use siblings.append 
#siblings[6] = 'Mayo'
print(siblings)
# Slicing on a list
print(f'{siblings[:2]}')
# List position parameter start at zero
siblings.insert(2,"Chuy")
siblings.insert(3,43)
print(siblings)
siblings[2]
siblings.pop(1)
siblings.pop(0)
print(siblings)
print(f'Number of elements on siblings list: {len(siblings)}')

# Multi-dimensional list
cartesianCoords = [[0,0],[1,1],[1.5,2],[2,3]]
print(cartesianCoords)
print(r'Element 2 of cartesian-coords: {cartesianCoords[2]}')
print(f'Element 2 of cartesian-coords: {cartesianCoords[2]}')
cartesianCoords.pop(len(cartesianCoords)-1)
print(cartesianCoords)
cartesianCoords[2][0]

# Make a list out of a string
list("Maldonado")
lastName = list("Maldonado")
print(f'Number of chars in Maldonado: {len(lastName)}')

# Check to see if a particular element exists in the list
# using keyword "in"
'a' in lastName

# Create an empty list
hostName = []
hostName.append('csac-lin2')
mydomain = ['.','C','S','A','C','.','C','A','.','G','O','V']
hostName.extend(mydomain)
print(f'{hostName}')

"csac-gds" in hostName
"CSAC-LIN2" in hostName
"csac-lin2" in hostName

# Printing elements from a list
matrix = [[1,2,3],[4,5,6],[7,8,9]]
first_col = [row[0] for row in matrix]
print(first_col)

# Enumerate is a built - in function of Python. t allows us to loop over
# something and have an automatic counter.
fruits = ['apple', 'banana', 'orange', 'papaya', 'grapes']

# Another use case for enumerate
for enum_counter, i in enumerate(range(5), 1):
    print(f"{enum_counter}: {random.choice(fruits)}")

fruit_list = list(enumerate(fruits, 1))
# output: [(1, 'apple'), (2, 'banana'), ...]
print(f"Enumerated List: {fruit_list}")

print("# ---------------------------- Dictionaries -------------------------------")
# Dictionary - aka Hashtable, allows mapping/binding of key-values pairs
mail_server = {}
mail_server["node1"] = "mail1"
mail_server["node2"] = "mail2"
mail_server["IP1"] = '10.0.1.10'
mail_server["IP2"] = '10.0.1.20'
print(mail_server)
print( mail_server["node1"])
del mail_server["node1"] 
print(mail_server)
mail_server['node2'] = 'lodi-oda1'
print(mail_server.keys())
print(mail_server.values())

my_servers = {"node1":10,"node2":20, 'node3':{'mx':[30,40,50]}}
print(my_servers)
print(my_servers['node3'])
print(my_servers['node3']['mx'][2])

myName ="hector"
myName=myName.upper()
print(myName)
print(myName.lower())

print("# ------------------------ Tuples, Sets, and Booleans ------------------------")
# Tuples are immutable lists/arrays, which means that you can't alter its items.
siblings = ("Tono", "Yola", 'Chava')
print(siblings)
print(siblings[0])
#siblings[3] = 'Dani' # This fails because Tuples are immutable
print(siblings)
# Nested tuple, or multi-dimensional
siblings =(("Tono",57),("Yola",56),('Chava',55))
print(siblings)
print(siblings[2])
print(siblings[2][0])

# Create an empty tuple
city = ()

# * * * Sets * * *
# Un-ordered collection of unique elements
x = set()
x.add(1)
x.add(9.81)
x.add('H')
# Printing a set ea. time a different order will print
print(x)

# * * * Booleans * * *
# In Python these situations return False and instances
# which signal they are empty
"", 0, 0.0, 0j, [], (), {}, False, None

if True:
    print("Boolean is True!")

earth_is_flat = False
if (earth_is_flat):
    print("Galileo was wrong about the earth being not being at the \r \
            center of the universe.")
else:
    print("Galileo was right, the earth is not at center of universe.")

if 0:
    print(f"Boolean 0 is False!")
elif 1:
    print("Boolean 1 is True!")
else:
    print("0 and 1 are not booleans!")

print("# -------------------- Control Flow - Loops - IF-ElIF-ELSE --------------------")



print("# ---------------------------- Functions -------------------------------")
"""Functions allow you to repeat logic an infinite number of times without
   re-writting the same logic.
   
   Call the dir() to see what objects are available. when we create our own,
   we will see them when we call the dir() function."""
print(dir())


# Imputs/Arguments
   #args -- tuple of anonymous arguments
   #kwargs -- dictionary of named arguments
def f(*args, **kwargs):
   print('args: ', args, ' kvargs: ', kwargs)
   
f(1,2,3, Jan=1,Feb=2,Mar=3)

def ping():
    pass # pass

print(ping())

# math module has already been imported above, check what objects are available
print(dir(math))

def vol_sphere(r):
    """Returns the volume of a sphere with radius r."""
    v = (4.0/3.0) * math.pi * r**3
    return v

help(vol_sphere) # How to use the function
print(vol_sphere(2))

def triangle_area(b, h):
    """Returns the area of a triangle with base b and height h."""
    return 0.5 * b * h

print(triangle_area(3, 6))

# Keyword Arguments
def cm(feet = 0, inches = 0):
    """Converts a lengthform fee and inches to centimeters."""
    inches_to_cm = inches * 2.54
    feet_to_cm = feet * 12 * 2.54
    return inches_to_cm + feet_to_cm

print(f"Feet to centimeters: {cm(feet = 5)}" )
print(f"Inches to centimeteters: {cm(inches = 70)}")
print(f"Feet  and inches to centimeters: {cm(feet = 5, inches = 8)}")
# Reverse the keyworkd arguments.  Keyword arguments allows flexible functions
# and clean code.
print(f"Feet  and inches to centimeters: {cm(inches = 8, feet = 5)}")

"""Types of arguments
    - keywords and required
    -- required arguments are not given a name, but identified by position.
    If both are used, keyword arguments must come last.  Python calls keyword
    arguments default arguments."""
def g(y, x = 0):
    return x + y

print(g(5)) # Only the required y argument
print(g(7, x = 3))

# ------------------------ List Comprehensions ---------------------------
print("# ---------------------------- List Comprehensions -------------------------------")
"""
List Comprehensions
===================
List comprehensions provide a concise way to create lists. 

It consists of brackets containing an expression followed by a for clause, then
zero or more for or if clauses. The expressions can be anything, meaning you can
put in all kinds of objects in lists.

The result will be a new list resulting from evaluating the expression in the
context of the for and if clauses which follow it. 

The list comprehension always returns a result list.

List comprehension is an elegant way to define and create list in python.
We can create lists just like mathematical statements and in one line only.

[expr for val in collection]
[expr for val in collection if <tests>]
[expr for val in if <test1> and <test2>]
[expr for val1 in collection1 and val2 in collection2]
"""
# fv_list is a list that will contain the compound interest earned ea. year
# for three years at 1%  interest rate.  Using the
# future_value =Pe^rt function.
# Output expression = (500*math.e**(0.01*t))
# Input expression = range(1,4)
# t = is the variable for time in years
# 'for t in' is the predicate.
fv_list = [(500*math.e**(0.01*t)) for t in range(1,4)] # Code executes from 1-3 not 4
print(f"List comprehension: {fv_list}")
print(fv_list[2])

# Less elegant, but is the same
fv_lst = []
for t in range(1,4):
    fv_lst.append((500*math.e**(0.01*t)))

print(fv_lst)

# List
movies = [("Citizen Kane", 1941), ("Spirited Away", 2001), ("It's a Wonderful Life", 1946), ("Gattaca", 1997),
          ("Rear Window", 1954),("The Lord of the Rings: The Fellowship of the Ring", 2001),("Rocky", 1976)]
#Ex. 1
pre2k = [title for (title, year) in movies if year < 2000]
pprint(pre2k)

# Scalar Multiplication
vector1 = [2, -3, 1]
w = [4*x for x in vector1]
print(w)

# Cartesian Product
# If A and B are sets, then the Cartesian product is the set of pairs (a, b)
# where 'a' is in A and 'b' is in B.
# A x B = {(a,b) | a E A, b E B}
# A = {1, 3}
# B {m,y}
# A x B = {(1,m), (1, y), (3, m), (3, y)}
A = [1, 3, 5, 7]
B = [2, 4, 6, 8]

cartesian_product = [(a,b) for a in A for b in B]
print(cartesian_product)
# ---------------------------- End of File -------------------------------
print("\n--------------- Program Completed! ---------------\n")