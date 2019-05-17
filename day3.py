#!/usr/bin/env python3
"""Problem - Day 3
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
For example, given the following Node class
    class Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
The following test should pass:
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
"""
import sys


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def buildNode(self, val):
        return None if val == '#' else Node(val)

    def serialize(self, root, subnode=False):
        if type(root) is not Node:
            print('not a node')
            sys.exit()
        ser = [root.val]
        if root.left is not None:
            ser += self.serialize(root.left, True)
        else:
            ser.append('#')
        if root.right is not None:
            ser += self.serialize(root.right, True)
        else:
            ser.append('#')
        if subnode is True:
            return ser
        else:
            return ':'.join(ser)

    def deserialize(self, data):
        dlist = data.split(':')
        dlist.reverse()
        setattr(self, 'dlist', dlist)
        node = self._tree_create()
        return node

    def _tree_create(self):
        node = self.buildNode(self.dlist.pop())
        if node is None:
            return node
        node.left = self._tree_create()
        node.right = self._tree_create()
        return node


if __name__ == '__main__':
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    codec = Codec()
    try:
        assert codec.deserialize(codec.serialize(node)).left.left.val == 'left.left'
    except AssertionError:
        print('Failed')
        sys.exit()

    print('Passed')
