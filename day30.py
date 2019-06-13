#!/usr/bin/env python3
"""Problem - Day 30
You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.
Compute how many units of water remain trapped on the map in O(N) time and O(1) space.
For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.
Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.
"""
def findVol(m):
    if len(m) <= 2:
        return 0
    left = m[0]
    right = m[-1]
    vol = 0
    if left <= right:
        current = 1
        while left > m[current]:
            vol += left - m[current]
            current += 1
        return findVol(m[current:]) + vol
    else:
        current = -2
        while right > m[current]:
            vol += right - m[current]
            current -= 1
        return findVol(m[:current + 1]) + vol


def main():
    m1 = [2, 1, 2]
        # |     | #
        # |  |  | #
        ###########
    result1 = findVol(m1)
    assert result1 == 1

    m2 = [3, 0, 1, 3, 0, 5]
        #                | #
        #                | #
        # |        |     | #
        # |        |     | #
        # |     |  |     | #
        ####################
    result2 = findVol(m2)
    assert result2 == 8

    m3 = [7, 2, 3, 8, 3, 1, 9, 7, 4, 2]
        #                   |          #
        #          |        |          #
        # |        |        |  |       #
        # |        |        |  |       #
        # |        |        |  |       #
        # |        |        |  |  |    #
        # |     |  |  |     |  |  |    #
        # |  |  |  |  |     |  |  |  | #
        # |  |  |  |  |  |  |  |  |  | #
        ################################
    result3 = findVol(m3)
    assert result3 == 21

    m4 = [2, 4, 7, 9, 1, 3, 8, 3, 2, 7]
        #          |                   #
        #          |        |          #
        #       |  |        |        | #
        #       |  |        |        | #
        #       |  |        |        | #
        #    |  |  |        |        | #
        #    |  |  |     |  |  |     | #
        # |  |  |  |     |  |  |  |  | #
        # |  |  |  |  |  |  |  |  |  | #
        ################################
    result4 = findVol(m4)
    assert result4 == 21


if __name__ == '__main__':
    main()
