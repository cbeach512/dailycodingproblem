#!/usr/bin/env python3
"""Problem - Day 13
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""
def longest_sub(s, k):
    current_max = 0
    for e in enumerate(s):
        if len(s[e[0]:]) < current_max:
            break
        d_chars = set()
        sub_len = 0
        for i in s[e[0]:]:
            d_chars.add(i)
            if len(d_chars) > k:
                break
            sub_len += 1
            if sub_len > current_max:
                current_max = sub_len
    return current_max

if __name__ == '__main__':
    s = input('string: ')
    k = int(input('max distinct characters: '))
    print(longest_sub(s, k))

