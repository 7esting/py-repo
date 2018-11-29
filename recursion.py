"""
Recursion: factorials, Fibonacci, & Memorization
"""
# ----------- Import Packages, and/or Modules: Classes, & Functions -----------
from functools import lru_cache # Least Recently Used Cache
import datetime
import math

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
# This function is good for small range of numbers, unless we use lru_cache
# decorator to add memorization
@lru_cache(maxsize=1000)
def fibonacci(n):
    """
    n fibonacci # 1, 1, 2, 3, 5
    - -----------
    1 return 1
    2 return 1
      Third fibonacci {(n-1) + (n-2)} <=> {(2-1 = 1) + (2 - 2 = 0)} ==> 2 + 0 = 2
    3 Fourth Fibonacci {(n-1) + (n-2)} <=> {(3-1 = 2) + (3 - 2 = 1)} ==> 2 + 1 = 3
    4 Fifth Fibonacci {(n-1) + (n-2)} <=> {(4-1 = 3) + (4 - 2 = 2)} ==> 3 + 2 = 5
    """
    # What would happen if we called the fibonacci function and passed it a
    # non-positive int?  It errors.
    if type(n) != int:
        raise TypeError("n must be a positive integer.")
    if n < 1:
        raise ValueError("n must be a positive integer.")

    # Compute Nth term
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)


"""
Memorizaiton
------------
Idea: Cache values

Optimize our fibonacci function for large 
"""
# Memorization method 1: Implement explicitly
fibonacci_cache = {}
def fibonacci_memorization_v1(n):
    #If we have cached the value, then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # Compute the Nth term
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        value = fibonacci_memorization_v1(n-1) + fibonacci_memorization_v1(n-2)

    # Cache the value and return it
    fibonacci_cache[n] = value
    return value

# Memorization method 2: Using Python builtin tool lru_cache decorator
# ~  Update fibonacci(n) function to use this decorator


def main():
    """"Main program function calls."""
    x_factorial = factorial(5)
    print(x_factorial)

    # Runs forever! Unless we use lru_cache decorator
    # for n in range(1, 1001):
    #     print(f"{n} : {fibonacci(n)}")

    # Test with non-int values
    #print(fibonacci("one"))
    #print(fibonacci("-5"))

    # for n in range(1, 1001):
    #     print(f"{n} : {fibonacci_memorization_v1(n)}")

    # The golden ratio, by taking the ratio of fibonacci consecutive terms
    for n in range(1, 51):
        print(fibonacci(n+1) / fibonacci(n))

# Application entry point
if __name__ == '__main__':
    main()
