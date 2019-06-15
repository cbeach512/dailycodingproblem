#!/usr/bin/env python3
"""Problem - Day 31
The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.
Given two strings, compute the edit distance between them.
"""
def eDist(a, b):
    a_len = len(a)
    b_len = len(b)
    dist = list()
    for a_pos in range(a_len + 1):
        dist.append(list())
        for b_pos in range(b_len + 1):
            if a_pos == 0:
                dist[a_pos].append(b_pos)
            elif b_pos == 0:
                dist[a_pos].append(a_pos)
            elif a[a_pos - 1] == b[b_pos - 1]:
                dist[a_pos].append(dist[a_pos - 1][b_pos - 1])
            else:
                dist[a_pos].append(1 + min(
                    dist[a_pos - 1][b_pos - 1],
                    dist[a_pos][b_pos - 1],
                    dist[a_pos - 1][b_pos]
                ))
    return dist[a_len][b_len]


def main():
    tests = [
        ('kitten', 'sitting', 3),
        ('small', 'tall', 2),
        ('accept', 'except', 2),
        ('cereal', 'serial', 2),
        ('pear', 'pair', 2),
        ('abcdefg', 'higklmn', 7),
        ('abcdefg', 'abcdcba', 3),
        ('abcdefg', 'gfedefg', 3),
        ('abcdefg', 'abcdefg', 0),
        ('abcdefg', 'abxyzfg', 3),
        ('abcdefg', 'axcyezg', 3)
    ]
    for a, b, d in tests:
        assert eDist(a, b) == d


if __name__ == '__main__':
    main()

