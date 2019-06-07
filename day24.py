#!/usr/bin/env python3
"""Problem - Day 24
Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.
Design a binary tree node class with the following methods:
- is_locked, which returns whether the node is locked
- lock, which attempts to lock the node. If it cannot be locked, then it should return false. Otherwise, it should lock it and return true.
- unlock, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise, it should unlock it and return true.
You may augment the node to add parent pointers or any other property you would like. You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes. Each method should run in O(h), where h is the height of the tree.
"""
T = True
F = False


class LockNode():
    def __init__(self, value, parent=None):
        self.v = value
        self.p = parent
        self.c = None
        self._l = F

    def is_locked(self):
        '''is_locked, which returns whether the node is locked'''
        return self._l

    def lock(self):
        '''
        lock, which attempts to lock the node. If it cannot be locked, then
        it should return false. Otherwise, it should lock it and return
        true.
        '''
        if self._l:
            return F
        if self._p_lock_check():
            return F
        if self._c_lock_check():
            return F
        self._l = T
        return T

    def unlock(self):
        '''
        unlock, which unlocks the node. If it cannot be unlocked, then it
        should return false. Otherwise, it should unlock it and return
        true.
        '''
        if not self._l:
            return F
        if self._p_lock_check():
            return F
        if self._c_lock_check():
            return F
        self._l = F
        return T

    def _p_lock_check(self):
        '''
        if any parent is locked, return true
        '''
        if self.p.is_locked():
            return T
        try:
            if self.p._p_lock_check():
                return T
        except AttributeError:
            pass
        return F

    def _c_lock_check(self):
        '''
        if any parent is locked, return true
        '''
        if self.c.is_locked():
            return T
        try:
            if self.c._c_lock_check():
                return T
        except AttributeError:
            pass
        return F

    def add_child(self, child):
        '''
        creates a child node with self as parrent
        returns the child node
        '''
        self.c = LockNode(child, self)
        return self.c


def main():
    top = LockNode('top')
    upper = top.add_child('upper')
    middle = upper.add_child('middle')
    lower = middle.add_child('lower')
    bottom = lower.add_child('bottom')

    assert middle.lock()
    assert not middle.lock()
    assert not upper.lock()
    assert not lower.lock()
    assert middle.unlock()
    assert not middle.unlock()


if __name__ == '__main__':
    main()

