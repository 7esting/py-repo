# -----------------------------------------------------------------------------
# File Name: fn_except.py
# Dependencies: None
# Purpose: Script demonstrates definitions of Functions, and exception handling.
#          This script/program will have two Functions and a main. One that will
#          accept user input and the other will print to screen.
#
# Change Log:
#
# Name                 Date       Comment
# ----------------     ---------  ---------------------------------------------
# Hector Maldonado     7/22/2018  Created script/program
# Sebastian Maldonado  7/22/2018  Added Functions to convert celsius to 
#                                 fahrenheit. At lease one of the Functions will
#                                 return a value. Also, modified program to
#                                 present menu options.                            
# -----------------------------------------------------------------------------

# ---------------------------- Import Libraries -------------------------------
import os
import sys

# ---------------------------- Global Variables -------------------------------
usrStr = ""

# ---------- User Input Function ----------
# Only accept strings less than 81 characters long.
def get_userInput():
    maxStrLength = 80
    try:
        usrStr = raw_input("Enter a string less than 81 characters long: ")
        #usrStr = sys.stdin.read()
        usrStr += '\n'
        
        if len(usrStr) <=  maxStrLength:
            put_userInput(usrStr)
        else:
            outError = "String doest not meet required length, max 80 characters."
            outError += " String Length: "
            outError += str(len(usrStr))
            print (outError)
            #exit(0) #causes exception to be raised

    except:
        print ("Unknown error occurred!")
        #raise
        pass 

# ---------- Output Function ----------
def put_userInput(usrStr):
    print (usrStr)

# ---------- cel2fahr Function ----------
"""Returns temperature in degrees Fahrenheit"""
def cel2fahr(tCelcius):
    return (float(tCelcius * 9 / 5) + 32)

# ---------------------------- Main Function -----------------------------------
def main():
    #os.system("/usr/bin/clear")
    os.system("cls")
    # Menu loop
    while True:
        print ("\n\t* * * Menu * * *\n")
        print ("0. Clear Screen")
        print ("1. String Length Test")
        print ("2. Celcius to Fahrenheit")
        print ("3. Exit\n")
        # raw_input() does not work with int numbers
        #response = raw_input("Menu Selection: ")
        response = input("Menu Selection#: ")
        response = int(response)
        print (response)
        
        if response == 1:
            get_userInput()

        if response == 2:
            while True:
                try:
                    # Cast string from input() to a float
                    tCelcius = float(input("Enter temperature in degrees Celcius: "))
                    print ("Celcius: ", tCelcius, " => ", "Fahrenheit: ", cel2fahr(tCelcius))
                    break
                except NameError:
                    print ("\t!Not a valid float value!, Please try again...")
                except SyntaxError:
                    print ("\t!Not a valid float value!, Please try again...")
                except ZeroDivisionError as e:
                    print (e)
                except:
                    print("Unexpected error:", sys.exc_info()[0])
                    raise

        if response == 0:
            os.system("/usr/bin/clear")
            #os.system("cls")

        if response == 3:
            print ("Bye!")
            break
# ---------------------------- End Main Function ------------------------------

# Application entry point
if __name__ == "__main__":
    main()
# ----------------------- End of file in script/program -----------------------
 