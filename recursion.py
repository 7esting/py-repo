"""
Recursion: factorials, Fibonacci, & Memorization
"""
# ----------- Import Packages, and/or Modules: Classes, & Functions -----------
import datetime

# --------------------------- Function Definitions ----------------------------
# Factorial function
def factorial(n: int):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

# Test
def calc_age(dob: int):
    print(type(dob))
    dob = int(dob)
    return datetime.date.today().year - dob

def main():
    """"Main program function calls."""
    x_factorial = factorial(5)
    print(x_factorial)

    resp = input("Year of Birth (yyyy): ")
    print(calc_age(resp))

# Application entry point
if __name__ == '__main__':
    main()
