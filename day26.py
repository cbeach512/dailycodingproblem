#!/usr/bin/env python3
"""Problem - Day 26
Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.
The list is very long, so making more than one pass is prohibitively expensive.
Do this in constant space and in one pass.
"""
class Node():
    def __init__(self, val, next_node=None):
        self.val = val
        self.n_node = next_node

    def add_node(self, val):
        self.n_node = Node(val)
        return self.n_node

    def __str__(self):
        l = []
        cur = self
        while cur:
            l.append(str(cur.val))
            cur = cur.n_node
        return ' => '.join(l)


def remove_nth_from_last(head, nth):
    """
    Give the leader a nth + 1 headstart, and have follower chase. Once Leader
    is at the end, have follower sets it's next node value to skip it's current
    next node.

    returns the head node of the modified linked list.
    """
    leader = head
    for _ in range(nth + 1):
        try:
            leader = leader.n_node
        # occurs when the nth node from the end is the head node
        except AttributeError:
            head = head.n_node
            return head
    follower = head
    while leader:
        leader = leader.n_node
        follower = follower.n_node
    follower.n_node = follower.n_node.n_node
    return head


def main():
    head = Node(0)
    cur = head
    for i in range(1,10):
        n_node = cur.add_node(i)
        cur = n_node
    print(head)
    # remove a value in the middle
    remove_nth_from_last(head, 4)
    print(head)
    # remove the last value
    remove_nth_from_last(head, 1)
    print(head)
    # remove the first value
    head = remove_nth_from_last(head, 8)
    print(head)


if __name__ == '__main__':
    main()

