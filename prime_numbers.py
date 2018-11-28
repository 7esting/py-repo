import time
from math import sqrt, floor

"""
* * * EXAMPLE OF OPTIMIZING CODE/ALGORITHM * * *

Prime Numbers
-------------
Central to field of number theory. A key ingredient in cryptographic methods, i.e rsa algorithim.

Prime Number: Only divisible by itself and 1
				(2, 3, 5, 7, 11, 13, 17, 19, ...)

Composite Number: Can be factored into smaller integers
				(4=2x2, 6=2x3, 8=2x2x2, 9=3x3, ...)

Unit: 1 is neither prime nor composite

What are pseudo primes?
"""

# v.0.1 Test all divisors form 2 through n-1
# (skip 1 and n since every number is divisible by itself and 1)


def is_prime_v1(n):
    """Return 'True' if 'n' is a prime number.  False otherwise."""
    if n == 1:
        return False  # 1 is not prime

    for d in range(2, n):  # with the range(start, end, [increment]) function the last integer is not included.
        if n % d == 0:
            return False

    return True

def is_prime_v2(n):
    """Return 'True if 'n' is a prime number. False otherwise."""
    if n == 1:
        return False # 1 is not prime

    max_divisor = floor(sqrt(n))
    for d in range(2, 1 + max_divisor):
        if n % d == 0:
            return False
    return True

# More optimizations to is_prime_v2
# Step 1: Test if n is even
# Step 2: Test only odd divisors
def is_prime_v3(n):
    """Return 'True if 'n' is a prime number. False otherwise."""
    if n == 1:
        return False # 1 is not prime

    # If it's even and not 2, then it's not prime
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False

    max_divisor = floor(sqrt(n))
    for d in range(3, 1 + max_divisor, 2):
        if n % d == 0:
            return False
    return True

def main():
    """Call all functions from main"""
    # ===== Test Function
    # for n in range(1, 21):
    # print(n, is_prime_v1(n))

    # Test1: Computation speed
    t0 = time.time()
    for n in range(1, 100000):
        is_prime_v1(n)
    t1 = time.time()
    print(f"Time required without optimizations: {t1 - t0}") # Time required: 27.473999977111816

    # Test 2: Reduce number of divisors checked in the for-loop, we will only test
    # all devisors from 2 through sqrt(N).
    # 36 = 1 x 36
    #    = 2 x 18
    #    = 3 x 12
    #    = 4 x 9
    #    = 6 x 6  # is a perfect sqrt of 36
    #    = 9 x 4
    #    = 12 x 3
    #    = 18 x 2
    #    = 36 x 1
    #
    # To improve algorithm,
    # n = 1 x
    #   = a x b
    #   = ...
    #   = sqrt(n) * sqrt(n) # sqrt(36) * sqrt(36)

    # Test2: Computation speed
    t0 = time.time()
    for n in range(1, 100000):
        is_prime_v2(n)
    t1 = time.time()
    print(f"Time required with some optimization: {t1 - t0}") # Time required: 0.2049999237060547

    # Test3: Computation speed
    t0 = time.time()
    for n in range(1, 100000):
        is_prime_v3(n)
    t1 = time.time()
    print(f"Time required with more optimazation: {t1 - t0}") # Time required: 0.11299991607666016

# Application entry point
if __name__ == '__main__':
    main()