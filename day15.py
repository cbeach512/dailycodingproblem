#!/usr/bin/env python3
"""Problem - Day 15
Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
"""
import random

def get_rand_element(elements: list):
    rand_element = random.choices(elements)[0]
    return rand_element

if __name__ == '__main__':
    big_list = [i for i in range(100)]
    rand_element = get_rand_element(big_list)
    print(rand_element)

