#!/usr/bin/env python3
"""Problem - Day 32
Suppose you are given a table of currency exchange rates, represented as a 2D array. Determine whether there is a possible arbitrage: that is, whether there is some sequence of trades you can make, starting with some amount A of any currency, so that you can end up with some amount greater than A of that currency.
There are no transaction costs and you can trade fractional quantities.
"""
from math import log


def can_arb(t):
    g = [[-log(i) for i in row] for row in t]
    g_len = len(g)
    min_d = [float('inf')] * g_len
    min_d[0] = 0
    for _ in range(g_len - 1):
        for r in range(g_len):
            for c in range(g_len):
                if min_d[c] > min_d[r] + g[r][c]:
                    min_d[c] = min_d[r] + g[r][c]
    for r in range(g_len):
        for c in range(g_len):
            if min_d[c] > min_d[r] + g[r][c]:
                return True
    return False


def main():
    t1 = [[2, 4, 1, 1, 2], [4, 2, 5, 5, 1], [1, 2, 4, 1, 3], [4, 4, 3, 4, 3], [2, 1, 3, 5, 1]]
    assert can_arb(t1)

    t2 = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
    assert not can_arb(t2)


if __name__ == '__main__':
    main()

