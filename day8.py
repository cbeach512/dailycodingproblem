#!/usr/bin/env python3
"""Problem - Day 8
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""
class Node():
    def __init__(self, val, left=None, right=None):
        self.v = val
        self.l = left
        self.r = right

    def is_unival(self):
        try:
            if self.l.v == self.r.v:
                return True
        except AttributeError:
            if self.l == None and self.r == None:
                return True
        return False

    def univaltreecheck(self, count=None):
        if count is None:
            count = 0
        try:
            if self.is_unival():
                count += 1
        except AttributeError:
            return count
        try:
            count = self.l.univaltreecheck(count)
        except AttributeError:
            pass
        try:
            count = self.r.univaltreecheck(count)
        except AttributeError:
            pass
        return count

if __name__ == '__main__':
    n = Node
    n1 = n(0, n(1), n(0, n(1, n(1), n(1)), n(0)))
    print(n1.univaltreecheck())
