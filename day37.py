#!/usr/bin/env python3
"""Problem - Day 37
The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.
For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.
You may also use a list or array to represent a set.
"""
F = frozenset


def pwrSet(s):
    psl = [[]]
    for i in s:
        psl.extend([sub + [i] for sub in psl])
    return set(map(frozenset, psl))


def main():
    s1 = {1, 2, 3}
    assert pwrSet(s1) == {F(), F([1]), F([2]), F([3]), F([1, 2]),
                          F([1, 3]), F([2, 3]), F([1, 2, 3])}

    s2 = {1, 2, 3, 4}
    assert pwrSet(s2) == {F(), F([1]), F([2]), F([3]), F([4]), F([1, 2]),
                          F([1, 3]), F([1, 4]), F([2, 3]), F([2, 4]),
                          F([3, 4]), F([1, 2, 3]), F([1, 2, 4]), F([1, 3, 4]),
                          F([2, 3, 4]), F([1, 2, 3, 4])}

    s3 = {1, 2, 3, 4, 5}
    assert pwrSet(s3) == {
        F(), F([1]), F([2]), F([3]), F([4]), F([5]), F([1, 2]), F([1, 3]),
        F([1, 4]), F([1, 5]), F([2, 3]), F([2, 4]), F([2, 5]), F([3, 4]),
        F([3, 5]), F([4, 5]), F([1, 2, 3]), F([1, 2, 4]), F([1, 2, 5]),
        F([1, 3, 4]), F([1, 3, 5]), F([1, 4, 5]), F([2, 3, 4]), F([2, 3, 5]),
        F([2, 4, 5]), F([3, 4, 5]), F([1, 2, 3, 4]), F([1, 2, 3, 5]),
        F([1, 2, 4, 5]), F([1, 3, 4, 5]), F([2, 3, 4, 5]), F([1, 2, 3, 4, 5])
    }


if __name__ == '__main__':
    main()

