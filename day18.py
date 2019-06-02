#!/usr/bin/env python3
"""Problem - Day 18
Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.
For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:
- 10 = max(10, 5, 2)
- 7 = max(5, 2, 7)
- 8 = max(2, 7, 8)
- 8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.
"""
def maxSubArr(array, k):
    subArr = array[0:k-1]
    subArrMax = []
    for i in enumerate(array[k-1:]):
        subArr.append(i[1])
        subArrMax.append(max(subArr))
        del(subArr[0])
    return subArrMax


def main():
    a1 = [10, 5, 2, 7, 8, 7]
    k1 = 3
    print(maxSubArr(a1, k1))

    a2 = [17, 11, 17, 7, 17, 20, 4, 7, 1, 3, 19, 10, 10, 6, 14, 10, 13,
          2, 15, 6, 2, 15, 12, 8, 7, 10, 20, 11, 20, 10, 1, 20, 10, 13,
          15, 4, 20, 2, 8, 1, 15, 7, 20, 13, 1, 18, 4, 12, 14, 6, 7, 1,
          11, 19, 19, 19, 16, 12, 19, 14, 16, 5, 8, 2, 11, 16, 16, 6,
          14, 3, 20, 18, 1, 4, 6, 5, 4, 11, 6, 11, 3, 4, 8, 2, 10, 6,
          12, 3, 19, 15, 8, 13, 18, 4, 1, 3, 13, 20, 17, 2]
    k2 = 5
    print(maxSubArr(a2, k2))


if __name__ == '__main__':
    main()

