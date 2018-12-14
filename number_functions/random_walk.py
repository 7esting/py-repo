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
4 blocks or fewer from home?

Create two versions of a random walk function.
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


# ------------------------------- Main Function -------------------------------

## Main
# All functions are called in main.
# inputs: none
# returns: none
def main():
    # 25 Random walks
    for i in range(25):
        walk = random_walk(10) # Each walk  is 10 blocks from home
        # Sum of absulute value of x & y coordinates is the distance from home
        print(walk, "Distance from home = ",
              abs(walk[0]) + abs(walk[1]))

# ------------------------ Main Application Entry Point -----------------------
if __name__ == '__main__':
    main()
