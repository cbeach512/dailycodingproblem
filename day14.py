#!/usr/bin/env python3
"""Problem - Day 14
The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.
Hint: The basic equation of a circle is x2 + y2 = r2.

Notes:
    Assuming a circle with radias of 1 inside a square with sides of 2.
        Area of the circle = π * r^2 = π * 1^2 = π * 1 = π
        Area of the square = 2^2 = 4
        Any random point inside the square could be inside the cicle, the chance would be:
            area of the circle/area of the square
            or
            all points within the circle/all points total
        Calling all points T and points incide the circle C, I could say:
            area of the circle/area of the square = C/T
            or
            π / 4 = C / T
        So we can multiply both sides and get π = 4 * C / T
    To know if a point is inside the circle, it's distance from origin needs to be => the radias of the cirlce.
        we know r = 1, so r^2 is also 1
        distance from origin is x^2 + y^2
        as long as x^2 + y^2 is 1 or less, the point is inside the circle
    So, if we create a ton of points, a number close to pi should emerge with the follow equations.
        total = some high number
        inside = all points that are <= 1 when x & y are squared and added together
        pi = 4 * inside / total
    I did try counting points 'on the line' as counting as inside or not, all numbers calculated for pi were exactly the same... so it doesn't seem to make a differeance at this level of accuracy.
"""
import random

def pi_calc(num_points: int) -> float:
    inside_circle = 0
    for _ in range(num_points):
        x = random.random()
        y = random.random()
        if x ** 2 + y ** 2 <= 1: # find and count all random points inside the circle
            inside_circle += 1
    pi = 4 * inside_circle / num_points # should produce a number close to pi
    return pi

if __name__ == '__main__':
    num_points = 10 ** 6 # Higher power, should be more accurate
    pi = pi_calc(num_points)
    print('{0:.3f}'.format(pi))

