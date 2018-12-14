"""
Random Walk using Monte Carlo Simulation, or probability simulation, which is a
technique used to understand the impact of risk and uncertainty in financial,
project management, cost, and other forecasting models.

When you have a range of values as a result, you are beginning to understand
the risk and uncertainty in the model. The key feature of a Monte Carlo
simulation is that it can tell you – based on how you create the ranges of
estimates – how likely the resulting outcomes are.

Monte Carlo Simulation:
- A method of estimating the value of an unknown quantity using the principles
  of inferential statistics
- Inferential statistics
  ~ Population: a set of examples
  ~ Sample: a proper subset of a population
  ~ Key fact: a 'random sample' tends to exhibit the same properties as the
    population from which it is drawn

https://www.riskamp.com/files/RiskAMP%20-%20Monte%20Carlo%20Simulation.pdf
"""
# ----------- Import Packages, and/or Modules: Classes, & Functions -----------
import random

# --------------------------- Function Definitions ---------------------------
"""
Suppose that you live in a neighbor hood that is a perfect grid of squares.
What is the longest random walk you can take so that on average you will end up
4 blocks or fewer from home? Use the Monte Carlo method

Create two versions of a random walk function.

Random Walks can be used to simulate the movement of molecules in liquid, or
the Stock Market.
"""

def random_walk(n) -> "Return coordinates (x, y) as a tuple":
    """Return coordinates after 'n' block random walk."""
    x = 0
    y = 0
    for i in range(n):
        step = random.choice(['N', 'S', 'E', 'W'])
        if step == 'N':
            y += 1
        elif step == 'S':
            y -= 1
        elif step == 'E':
            x += 1
        else:
            x -= 1
    return (x, y)

def random_walk_v2(n) -> "Return coordinates after 'n' block random walk.":
    x, y = 0, 0
    for i in range(n):
        # dx 'difference in x'
        # dy 'difference in y'
        # EX. if we walk north one block ==> (0, 1)
        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        # x += dx <==> x = x + dx
        x += dx
        # y += dx <==> y = y + dy
        y += dy
    return (x, y)


# ------------------------------- Main Function -------------------------------

## Main
# All functions are called in main.
# inputs: none
# returns: none
def main():
    # ## 25 Random walks
    # for i in range(25):
    #     walk = random_walk(10)  # Each walk  is 10 blocks from home
    #     # Sum of absulute value of x & y coordinates is the distance from home
    #     print(walk, "Distance from home = ",
    #           abs(walk[0]) + abs(walk[1]))
    #
    # ## 25 Random walks
    # for i in range(25):
    #     walk = random_walk_v2(10)  # Each walk  is 10 blocks from home
    #     # Sum of absulute value of x & y coordinates is the distance from home
    #     print(walk, "Distance from home v2 = ",
    #             abs(walk[0]) + abs(walk[1]))

    ## To answer the question. What is the longest random walk you can take so
    # that on average you will end up 4 blocks or fewer from home? Use the
    # Monte Carlo method
    number_of_walks = 10000 # try 20K and compare results
    print(f"\n Monte Carlo Simulation:")
    for walk_length in range(1, 31):
        no_transport = 0 # Number of walks 4 or fewer from home
        for i in range(number_of_walks):
            (x, y) = random_walk_v2(walk_length)
            distance = abs(x) + abs(y)
            if distance <= 4:
                no_transport += 1

        no_transport_percentage = float(no_transport) / number_of_walks
        print(f"Walk size = {walk_length} / % of no transport = {100*no_transport_percentage}")

# ------------------------ Main Application Entry Point -----------------------
if __name__ == '__main__':
    main()
