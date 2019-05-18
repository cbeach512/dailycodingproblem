#!/usr/bin/env python3
"""Problem - Day 1
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
"""

L = [10,15,3,7]

def dcp(k, nums=L):
    for n in nums:
        n2 = k - n
        if n2 in nums:
            return True
    return False

if __name__ == '__main__':
    print(dcp(17))
