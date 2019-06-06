#!/usr/bin/env python3
"""Problem - Day 23
You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.
Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.
- For example, given the following board:
    [[f, f, f, f],
    [t, t, f, t],
    [f, f, f, f],
    [f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.
"""
T = True
F = False
N = (-1, 0)
S = (1, 0)
E = (0, 1)
W = (0, -1)


def get_out(maze, start, end, steps=0, prev_steps=[]):
    if len(prev_steps) > steps -1:
        prev_steps = prev_steps[:steps]
    if start == end:
        return steps
    if steps >= len(maze) * len(maze[0]):
        return steps
    prev_steps.append(start)
    total_steps = []
    for dir in [N, S, E, W]:
        dest = (start[0] + dir[0], start[1] + dir[1])
        if (-1 < dest[0] < len(maze) and -1 < dest[1] < len(maze[0])
            and not dest in prev_steps and not maze[dest[0]][dest[1]]):
            total_steps.append(get_out(maze, dest, end, steps + 1, prev_steps))
    try:
        return min(total_steps)
    except ValueError:
        return len(maze) * len(maze[0])


def main():
    maze1 = [[F, F, F, F],
            [T, T, F, T],
            [F, F, F, F],
            [F, F, F, F]]
    start1 = (3, 0)
    end1 = (0, 0)
    print(get_out(maze1, start1, end1))

    maze2 = [[F, F, F, F],
             [T, T, F, T],
             [F, F, F, F],
             [F, F, F, F]]
    start2 = (3, 3)
    end2 = (0, 0)
    print(get_out(maze2, start2, end2))

    maze3 = [[F, F, F, T, F, T, F, F, F],
             [T, T, F, T, F, T, F, T, F],
             [F, T, F, F, F, F, F, T, F],
             [F, T, T, T, F, T, F, T, F],
             [F, F, F, F, F, T, F, T, F],
             [T, T, T, T, F, T, T, T, T],
             [F, F, F, F, F, F, F, F, F],
             [F, T, F, T, T, T, T, T, F],
             [F, T, F, F, F, F, F, T, F]]
    start3 = (0, 0)
    end3 = (8, 8)
    print(get_out(maze3, start3, end3))


if __name__ == '__main__':
    main()

