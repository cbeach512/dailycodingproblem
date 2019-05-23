#!/usr/bin/env python3
"""Problem - Day 9
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
Follow-up: Can you do this in O(N) time and constant space?
"""
class SumList(list):
    def max_non_adj_sum(self):
        new_candidate = self[0]
        old_max = 0
        for i in self[1:]:
            new_max = max(old_max, new_candidate)
            new_candidate = old_max + i
            old_max = new_max
        return max(old_max, new_candidate)

if __name__ == '__main__':
    l1 = SumList([2, 4, 6, 2, 5])
    print(l1.max_non_adj_sum())

    l2 = SumList([5, 1, 1, 5])
    print(l2.max_non_adj_sum())

