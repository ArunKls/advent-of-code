import sys

f = open("day16.txt", "r")
data = f.readlines()
f.close()

count = 0

sys. setrecursionlimit(10000)


def dfs(row, col, dir, vis, visdir):
    if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
        return
    if (row, col, dir) in visdir:
        return
    vis.add((row, col))
    visdir.add((row, col, dir))
    # print(row, col, grid[row][col])
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # [d, r, u, l]
    if dir == 0:
        if grid[row][col] in ['-']:
            dfs(row, col-1, 3, vis, visdir)
            dfs(row, col+1, 1, vis, visdir)
        elif grid[row][col] in ['|', '.']:
            dfs(row+1, col, dir, vis, visdir)
        elif grid[row][col] in ['\\']:
            dfs(row, col+1, 1, vis, visdir)
        else:
            dfs(row, col-1, 3, vis, visdir)
    elif dir == 1:
        if grid[row][col] in ['|']:
            dfs(row-1, col, 2, vis, visdir)
            dfs(row+1, col, 0, vis, visdir)
        elif grid[row][col] in ['-', '.']:
            dfs(row, col+1, dir, vis, visdir)
        elif grid[row][col] in ['\\']:
            dfs(row+1, col, 0, vis, visdir)
        else:
            dfs(row-1, col, 2, vis, visdir)
    elif dir == 2:
        if grid[row][col] in ['-']:
            dfs(row, col-1, 3, vis, visdir)
            dfs(row, col+1, 1, vis, visdir)
        elif grid[row][col] in ['|', '.']:
            dfs(row-1, col, dir, vis, visdir)
        elif grid[row][col] in ['\\']:
            dfs(row, col-1, 3, vis, visdir)
        else:
            dfs(row, col+1, 1, vis, visdir)
    elif dir == 3:
        if grid[row][col] in ['|']:
            dfs(row-1, col, 2, vis, visdir)
            dfs(row+1, col, 0, vis, visdir)
        elif grid[row][col] in ['-', '.']:
            dfs(row, col-1, dir, vis, visdir)
        elif grid[row][col] in ['\\']:
            dfs(row-1, col, 2, vis, visdir)
        else:
            dfs(row+1, col, 0, vis, visdir)
    return

def runner(row, col, dir):
    vis = set()
    dfs(row, col, dir, vis, set())
    return len(vis)

grid = []
for line in data:
    grid.append(list(line.strip()))
# print(len(grid), len(grid[0]))


def part1():
    global count
    try:
        return runner(0, 0, 1)
    except Exception as e:
        print(e, count)


def part2():
    global count
    maxEnergized = 0
    try:
        for i in range(len(grid)):
            maxEnergized = max(maxEnergized, runner(i, 0, 1), runner(i, len(grid[0])-1, 3))
        for j in range(len(grid[0])):
            maxEnergized = max(maxEnergized, runner(0, j, 0), runner(len(grid)-1, j, 2))
        maxEnergized = max(maxEnergized, runner(0, 0, 0), runner(0, 0, 2), runner(0, len(grid[0])-1, 0), runner(len(grid)-1, len(grid[0])-1, 2))
    except Exception as e:
        print(e, count)
    return maxEnergized


if __name__ == "__main__":
    print(f"Answer for part one: {part1()}")
    print(f"Answer for part two: {part2()}")
