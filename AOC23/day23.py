from collections import deque
from copy import deepcopy

f = open("day23.txt", "r")
data = f.readlines()
f.close()


def part1():
    grid = []
    for line in data:
        line = list(line.strip())
        grid.append(line[:])
    for i in range(len(grid[0])):
        if grid[0][i] == '.':
            start = (0, i)
        if grid[len(grid)-1][i] == '.':
            end = (len(grid)-1, i)
    q = deque()
    q.append((start[0], start[1], [start], 0))
    maxsteps = 0
    next = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}
    while q:
        row, col, vis_old, steps = q.popleft()
        # print(row, col, vis_old)
        vis = deepcopy(vis_old)
        rows = [0, 0, 1, -1]
        cols = [1, -1, 0, 0]
        if (row, col) == end:
            print(steps)
            maxsteps = max(maxsteps, steps)
        if grid[row][col] == '.':
            for r, c in zip(rows, cols):
                nrow = row + r
                ncol = col + c
                if (nrow, ncol) not in vis and 0 <= nrow < len(grid) and 0 <= ncol < len(grid[0]) and grid[nrow][ncol] != '#':
                    vis.append((nrow, ncol))
                    q.append((nrow, ncol, vis, steps+1))
        else:
            nrow, ncol = row + next[grid[row][col]
                                    ][0], col + next[grid[row][col]][1]
            if grid[nrow][ncol] != '#' and (nrow, ncol) not in vis and 0 <= nrow < len(grid) and 0 <= ncol < len(grid[0]):
                vis.append((nrow, ncol))
                q.append((nrow, ncol, vis, steps+1))
    return maxsteps


def part2():
    grid = []
    for line in data:
        line = list(line.strip())
        grid.append(line[:])
    for i in range(len(grid[0])):
        if grid[0][i] == '.':
            start = (0, i)
        if grid[len(grid)-1][i] == '.':
            end = (len(grid)-1, i)
    q = deque()
    q.append((start[0], start[1], [start], 0))
    maxsteps = 0
    while q:
        row, col, vis_old, steps = q.popleft()
        # print(row, col, vis_old)
        vis = deepcopy(vis_old)
        rows = [0, 0, 1, -1]
        cols = [1, -1, 0, 0]
        if (row, col) == end:
            print(steps)
            maxsteps = max(maxsteps, steps)
        if grid[row][col] != '#':
            for r, c in zip(rows, cols):
                nrow = row + r
                ncol = col + c
                if (nrow, ncol) not in vis and 0 <= nrow < len(grid) and 0 <= ncol < len(grid[0]) and grid[nrow][ncol] != '#':
                    vis.append((nrow, ncol))
                    q.append((nrow, ncol, vis, steps+1))
    return maxsteps


if __name__ == "__main__":
    print(f"Answer for part one: {part1()}")
    print(f"Answer for part two: {part2()}")
