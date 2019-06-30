#!/usr/bin/env python3
"""Problem - Day 38
You have an N by N board. Write a function that, given N, returns the number of possible arrangements of the board where N queens can be placed on the board without threatening each other, i.e. no two queens share the same row, column, or diagonal.
"""
def q_configs(n, board=[]):
    if n == len(board):
        return 1
    count = 0
    for col in range(n):
        board.append(col)
        if q_safe(board):
            count += q_configs(n, board)
        board.pop()
    return count


def q_safe(board):
    q_row, q_col = len(board) - 1, board[-1]
    for row, col in enumerate(board[:-1]):
        diff = abs(q_col - col)
        if diff == 0 or diff == q_row - row:
            return False
    return True


def main():
    for n in range(10):
        print('{} {}'.format(n, q_configs(n)))


if __name__ == '__main__':
    main()

