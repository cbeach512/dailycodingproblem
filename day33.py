#!/usr/bin/env python3
"""Problem - Day 33
Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.
Recall that the median of an even-numbered list is the average of the two middle numbers.
For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:
    2
    1.5
    2
    3.5
    2
    2
    2
"""
from statistics import median


def main():
    l1 = [2, 1, 5, 7, 2, 0, 5]
    r1 = [median(l1[:i + 1]) for i in range(len(l1))]
    for i in r1:
        print('{0:.1f}'.format(i).rstrip('0').rstrip('.'))


if __name__ == '__main__':
    main()

