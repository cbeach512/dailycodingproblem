#!/usr/bin/env python3
"""Problem - Day 6
An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.
If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.
"""
# used to retreave object from pointer provided by id()
from ctypes import cast, py_object

class Node():
    """node for XorLinkedList object
    Attributes:
        val = value of the node
        both = xor of the previous and next objects in the xorlinkedlist
    """
    def __init__(self, val):
        self.val = val
        self.both = 0

class XorLinkedList():
    def __init__(self):
        self.head = self.tail = None
        self.__nodes = [] # required to avoid segfaults

    def add(self, node):
        """Like append for lists, always adds the new object to the end of the
        list of nodes.
        """
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.both = id(node) ^ self.tail.both
            node.both=id(self.tail)
            self.tail = node
            self.__nodes.append(node) # required to avoid segfaults

    def get(self, index):
        """loop through the list until the index is reached, and return the
        node.
        """
        prev_id = 0
        node = self.head
        next_id = 0
        for i in range(index):
            next_id = prev_id ^ node.both
            prev_id = id(node)
            node = cast(next_id, py_object).value
        return node

if __name__ == '__main__':
    # to test, first enter a space seperated list of values, followed by an
    # integer that would represent the target value in the list.
    # Example input:
    #     values: fe fi fo fum
    #     target: 3
    # Example output:
    #     fo
    xll = XorLinkedList()
    n = Node
    values = input('values: ').split()
    target = int(input('target: '))
    for item in enumerate(values):
        xll.add(n(item[1]))
    print(xll.get(target - 1).val)

