# -----------------------------------------------------------------------------
# File Name: pyClassObj.py
# Dependencies: None
# Purpose: My first Python class object.  Will be called by Main.py
#
# Change Log:
#
# Name                 Date       Comment
# ----------------     ---------  ---------------------------------------------
# Hector Maldonado     10/25/2018  Created script/program                    
# -----------------------------------------------------------------------------
# ---------------------------- Import Libraries -------------------------------
from datetime import date
from datetime import datetime

# ---------------------------- Class Definition -------------------------------

class Person:
    # Help doc text (docstring)
    """Note: The __init__() method/constructor is called automatically
    every time the class is being used to create/instanciate a new object from
    the Person class"""

    """A class used to represent a Person profile object.
            ...

            Attributes
            ----------
            full_name : str
                a persons full name
            birthday : str
                the person's date of birth
          
            Methods
            -------
            printMembers(self)
                Prints the person's age
    """

    # Initialization/Constructor - Initialize class attributes/fields
    def __init__(self, full_name, birthday):
        # full_name, and birthday are values provided to the Person object
        # self.name, and self.birthday are vars of the Person class
        self.name = full_name
        self.birthday = birthday # yyyymmdd
        # Default value if none is provided at object instanciation
        #self.birthday = "19740114"
        
        # Extract the first and last name
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

    # Instance methods
    """Functions inside a class are called methods."""
    #@property
    def age(self):
        """Doesn't consider leap-years"""
        today = date(2018, 11, 10)
        #today = date.today() # ==> datetime.date(2018, 11, 10)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = date(yyyy, mm, dd) # Date of birth
        age_in_days = (today - dob).days
        age_in_years = age_in_days / 365
        age_ = int(age_in_years)
        return print(f"DOB: {age_}")

## Instantiated p1 Object
p1 = Person("Sylvester      Stalone", "19460706")

print(f"\nName: {p1.last_name} \nDOB: {p1.birthday}")

#print(p1.getContact())
#print(r'Raw Text...%s' % p1.getContact())

p1.name = "Socratica"
print(p1.age)
print(p1.name)

# Call help class
help(Person)

print("\n********** Program completed! **********\n")