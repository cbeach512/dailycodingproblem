#!/usr/bin/env python3
"""Problem - Day 36
Given the root to a binary search tree, find the second largest node in the tree.
"""
class Node():
    def __init__(self, v):
        self.v = v
        self.l = None
        self.r = None

    def add_node(self, v):
        if v > self.v:
            self._add_r(v)
        else:
            self._add_l(v)

    def _add_r(self, v):
        if self.r:
            self.r.add_node(v)
        else:
            self.r = Node(v)

    def _add_l(self, v):
        if self.l:
            self.l.add_node(v)
        else:
            self.l = Node(v)


def buildTree(l):
    head = Node(l[0])
    for i in l[1:]:
        head.add_node(i)
    return head


def find2nd(head):
    cur = head
    pre = None
    while cur.r:
        pre = cur
        cur = cur.r
    if cur.l:
        pre = cur.l
        while pre.r:
            pre = pre.r
    return pre.v


def main():
    l1 = [14, 6, 95, 65, 97, 17, 3, 89, 10, 61, 67, 85, 4, 34, 98,
         75, 72, 79, 24, 76, 96, 84, 12, 47, 8, 82, 51, 70, 94, 48]
    head1 = buildTree(l1)
    assert find2nd(head1) == 97

    l2 = [3, 2, 1]
    head2 = buildTree(l2)
    assert find2nd(head2) == 2

    l3 = [1, 5, 2, 4, 3]
    head3 = buildTree(l3)
    assert find2nd(head3) == 4


    from random import randint
    l4 = [i for i in set([randint(1,10000) for _ in range(1000)])]
    head4 = buildTree(l4)
    assert find2nd(head4) == sorted(l4)[-2]


if __name__ == '__main__':
    main()

