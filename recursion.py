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

"""
Fibonacci Sequence: (After the 1, 1, the next number is the sum of the two
previous numbers.
ex. 1 + 1 = 2, 1 + 2 = 3
1, 1, 2, 3, 5, 8, ...

Goal: Write function to return the nth term of Fibonacci Sequence.
- Fast
- Clearly written
- Rock solid 
"""
def fibonacci(n):
    if n == 1:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    """"Main program function calls."""
    x_factorial = factorial(5)
    print(x_factorial)

    for n in range(1, 11):
        print(f"{n} : {fibonacci(n)}")

# Application entry point
if __name__ == '__main__':
    main()
