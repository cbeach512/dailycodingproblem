#!/usr/bin/env python3
"""Problem - Day 20
Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.
For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
In this example, assume nodes with the same value are the exact same node objects.
Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
"""
def findIntersect(list_a, list_b):
    for i in zip(list_a, list_b):
        if i[0] == i[1]:
            return i[0]


def main():
    la1 = [3, 7, 8, 10]
    lb1 = [99, 1, 8, 10]
    print(findIntersect(la1, lb1))


if __name__ == '__main__':
    main()

