"""
Socratica: 'The world is a chaotic place, from Heisenberg uncertainty principle to the butterfly effect our
            lives are fraught with randomness.'

Random Numbers can be used for many things such as
 - Add unpredictability to games
 - Cryptography
   Python WARNING: The pseudo-random generators of this module should not be used for
   security purposes.  Use os.urandom() or SystemRandom if you require a
   cryptographically secure pseudo-random number generator.
 - Monte carlo simulations
   ~ How to use Monte Carlo simulation to prove and find entropy with python?
   ~ https://github.com/neuropsychology/NeuroKit.py
"""
# ----------- Import Packages, and/or Modules: Classes, & Functions -----------
import random

# --------------------------- Function Definitions ---------------------------

def my_random():
    """
    Random, scale, shift my_random() -> random number in the interval [3, 7)
    """
    return 4 * random.random() + 3

# ------------------------------- Main Function -------------------------------

def main():
    pass

# ------------------------ Main Application Entry Point -----------------------
if __name__ == '__main__':
    main()
    # The random function represents the uniform distribution.  This means that
    # the probability of numbers being chosen are equaly spreadout over the
    # interval.  By default it returns numbers between [0, 1) zero
    # (including zero) to 1, but not including 1.
    for i in range(10):
        print(random.random())

    # Generate random numbers from interval [3, 7)
    # 1. Call random(): in [0, 1)
    # 2. Scale number (multiply by 4): in [0, 4)
    # 3. Shift number (add 3): in [3, 7)
    for i in range(10):
        rn = random.random()
        rn *= 4
        rn += 3
        print(f"\n{rn}")

        print(f"{my_random()}")

    help(my_random)

    print(f"\nRandom numbers that follow a normal distribution: \n ")
    # Another way to generate random numbers in any interval is by using the
    # random.uniform function.  The random.random() function can be used to
    # build customized random number generators.  It's the key ingredient in
    # many of the functions in teh random module.  The random() and uniform()
    # are both uniform distributions. But there are other distributions where
    # some group of numbers are more likely to be chosen than others, like
    # the Normal Distribution "Bell Curve" (Mean and Standard Deviation)

    for j in range(10):
        print(random.uniform(3,7))

    # Mean 5 with standard deviation 0.2
    for z in range(20):
        print(random.normalvariate(5,0.2))

    print(f"\nDiscrete random numbers: \n")
    # Discrete Probability Distributions
    # ~ Random numbers NOT from infinite possibilities
    # randint(min, max) # Random Integer

    for i in range(20):
        print(random.randint(1, 6))

    print(f"\nRandom elements from a list: \n")
    # Random element from a list
    outcomes = ["rock", 'paper', 'scissors']

    # Enumerate is a built - in function of Python. t allows us to loop over
    # something and have an automatic counter.
    for enum_counter, i in enumerate(range(20), 1):
        print(f"{enum_counter}: {random.choice(outcomes)}")