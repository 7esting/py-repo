#!/usr/bin/env LearnPythonNotes

# An alarm has a 4 digit code on a keypad [0-9] with 10 digits
# How many posible purmutations can we have, when order matters.
# Import libraries
##import math
from math import factorial
from math import sqrt as square_root

# Variables of sclar types and values:
# int 42, -3
# float 4.2, 3e8, 1.616e-35, float(7) ==> 7.0
# null object a=none, a is none ==> true

# Some math fuctions: 
#   abs() = Absolute value
#   floor() = round down
#   ceil() = round up
#
#   Add and assign one to tallyCount
#   tallyCount +=1

# bool True | False bool(0) = False, bool(42) = True, bool(-1) = True
# Bool operator can be used to determine if a list/array is empty in if and while loops statements
# bool ([]) = False, bool([1,2,3]) = True, bool("False") = True because list is not empty

# Convert float to int
k=int(4.0)
# int
n=10

P=factorial(n)/factorial(n-k)
print ("Number of purmutaions, where order matters to alarm code: ")
print (P)

print ("Square root of 81 is ")
print (square_root(81))

# Relational Operators, can be used to compare objects
# ==, !=, <, >, <=, >=

# * * * Remember that in Python you indent 4 spaces * * *
# Contidional Statements
nicoAge=42
chuyAge=43
lupeAge=46
if chuyAge < lupeAge:
    print("Chuy is younger than Lupe!")
elif nicoAge < chuyAge:
    print("Nico is younger than chuy!")
else:
    print("Hector's age is between Chuy's and Lupe's")

# Loops: while and for-loops
c = 5
# use the augmented oper -=, also available += and *=
#while expr:
#    print("loop while expr is true")
# Explicit is better than implicit (while c:)
while c != 0:
    print(c)
    c -=1

# Infinite while loop
#while True:
#    print ("Loop")
# Early breaks out of loops
t=100
while t!=500:
    print(t)
    t += 100
    if t == 300:
        print("\tBroke out of while loop\n")
        break

# While loop with user input
while True:
    print("Enter an int divisible by 7 to end loop: "),
    response = input()
    if int(response) % 7 == 0:
        break

vowels = ['a', 'e', 'i', 'o', 'u']
fname = "Guido"
fname = list(fname)

for v in vowels:
    for i in fname:
        if v == i:
            print(f"Vowel in {fname}: {v}")

if ('a' and 'e') or ('a' and 'i') in fname: # and, or does not work here
    print(f"Has vowels")
elif 'a' and 'e' in fname:
    print(f"Has 'a' & 'e' vowels.")
else:
    print(f"Conditions not met.")


