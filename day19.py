#!/usr/bin/env python3
"""Problem - Day 19
A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.
Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.
"""
def getMinColorCombo(matrix, prev_col=-1, house_num=0, cost=0):
    if house_num == len(matrix):
        return [cost]
    cost_list = []
    for i in range(len(matrix[0])):
        if i != prev_col:
            cost_list.extend(getMinColorCombo(matrix, i, house_num + 1, matrix[house_num][i] + cost))
    if prev_col == -1:
        return min(cost_list)
    return cost_list


def main():
    matrix1 = [[9, 6, 7, 7], [9, 9, 6, 3], [1, 8, 8, 9], [1, 6, 2, 5], [1, 6, 4, 1]]
    print(getMinColorCombo(matrix1))

    matrix2 = [[8, 8, 6, 4], [5, 2, 5, 1], [8, 1, 9, 5], [6, 7, 5, 5], [9, 1, 5, 9]]
    print(getMinColorCombo(matrix2))

    matrix3 = [[7, 2, 3, 1], [8, 9, 5, 1], [5, 9, 5, 9], [4, 5, 4, 1], [9, 5, 5, 3]]
    print(getMinColorCombo(matrix3))


if __name__ == '__main__':
    main()

