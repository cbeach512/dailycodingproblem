#!/usr/bin/env python3
"""Problem - Day 35
Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.
Do this in linear time and in-place.
For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
"""
R = 'R'
G = 'G'
B = 'B'


def prism(rgb):
    reds = 0
    greens = 0
    for i in range(len(rgb)):
        if rgb[-1] == R:
            rgb.insert(0, rgb.pop())
            reds += 1
        elif rgb[-1] == G:
            rgb.insert(reds, rgb.pop())
            greens += 1
        else:
            rgb.insert(reds + greens, rgb.pop())
    return rgb


def main():
    l1 = [G, B, R, R, B, R, G]
    assert prism(l1) == [R, R, R, G, G, B, B]

    l2 = [B, R, B, B, B, B, G, R, B, G,
          B, B, B, R, R, G, R, G, R, B]
    assert prism(l2) == [R, R, R, R, R, R, G, G, G, G,
                         B, B, B, B, B, B, B, B, B, B]


if __name__ == '__main__':
    main()

