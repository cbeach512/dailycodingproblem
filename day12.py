#!/usr/bin/env python3
"""Problem - Day 12
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.
For example, if N is 4, then there are 5 unique ways:
    - 1, 1, 1, 1
    - 2, 1, 1
    - 1, 2, 1
    - 1, 1, 2
    - 2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""
def unique_steps(n, steps=[1, 2]):
    if n in [0, 1]:
        return 1
    elif n < 0:
        return 0
    total_options = 0
    for step in steps:
        total_options += unique_steps(n - step, steps)
    return total_options

if __name__ == '__main__':
    print(unique_steps(4))
    print(unique_steps(4, [1, 3, 5]))

