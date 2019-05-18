#!/usr/bin/env python3
"""Problem - Day 4
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
You can modify the input array in-place.
"""
L1 = [3, 4, -1, 1]
L2 = [1, 2, 0]


def first_missing_pos(l):
    posl = sorted([n for n in l if n > 0])
    for n in enumerate(posl[1:]):
        if not n[1] == posl[n[0]] + 1:
            result = posl[n[0]] + 1
            return result
    result = posl[-1] + 1
    return result


if __name__ == '__main__':
    print(first_missing_pos(L1))
    print(first_missing_pos(L2))
