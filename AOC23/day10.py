from collections import deque

f = open("day10.txt", "r")
data = f.readlines()
f.close()


def part1():
    grid = []
    start = None
    for i, line in enumerate(data):
        line = list(line.strip())
        if not start:
            for j, char in enumerate(line):
                if char == "S":
                    start = (i, j)
        grid.append(line[:])

    def bfs(start):
        up = ['S', 'L', 'J', '|']
        down = ['S', '7', 'F', '|']
        left = ['S', '7', 'J', '-']
        right = ['S', 'L', 'F', '-']
        q = deque()
        q.append(start)
        step = 0
        vis = {start}
        while q:
            l = len(q)
            step += 1
            for i in range(l):
                # print(q)
                row, col = q.popleft()
                if grid[row][col] in down and row+1 < len(grid) and (row+1, col) not in vis and grid[row+1][col] in up:
                    q.append((row+1, col))
                    vis.add((row+1, col))
                if grid[row][col] in up and row-1 >= 0 and (row-1, col) not in vis and grid[row-1][col] in down:
                    q.append((row-1, col))
                    vis.add((row-1, col))
                if grid[row][col] in right and col+1 < len(grid[0]) and (row, col+1) not in vis and grid[row][col+1] in left:
                    q.append((row, col+1))
                    vis.add((row, col+1))
                if grid[row][col] in left and col-1 >= 0 and (row, col-1) not in vis and grid[row][col-1] in right:
                    q.append((row, col-1))
                    vis.add((row, col-1))
        return step-1

    return bfs(start)


def part2():
    grid = []
    start = None
    for i, line in enumerate(data):
        line = list(line.strip())
        if not start:
            for j, char in enumerate(line):
                if char == "S":
                    start = (i, j)
        grid.append(line[:])

    def bfs(start):
        up = ['S', 'L', 'J', '|']
        down = ['S', '7', 'F', '|']
        left = ['S', '7', 'J', '-']
        right = ['S', 'L', 'F', '-']
        q = deque()
        q.append(start)
        step = 0
        vis = {start}
        vislist = []
        start = 0
        end = -1
        while q:
            l = len(q)
            step += 1
            vislist.insert(start, q[0])
            start += 1
            if len(q) == 2:
                vislist.insert(end, q[1])
                end -= 1
            for i in range(l):
                # print(q)
                row, col = q.popleft()
                if grid[row][col] in down and row+1 < len(grid) and (row+1, col) not in vis and grid[row+1][col] in up:
                    q.append((row+1, col))
                    vis.add((row+1, col))
                if grid[row][col] in up and row-1 >= 0 and (row-1, col) not in vis and grid[row-1][col] in down:
                    q.append((row-1, col))
                    vis.add((row-1, col))
                if grid[row][col] in right and col+1 < len(grid[0]) and (row, col+1) not in vis and grid[row][col+1] in left:
                    q.append((row, col+1))
                    vis.add((row, col+1))
                if grid[row][col] in left and col-1 >= 0 and (row, col-1) not in vis and grid[row][col-1] in right:
                    q.append((row, col-1))
                    vis.add((row, col-1))
        return vis, vislist
    vis, vislist = bfs(start)
    ans = 0

    # Tried upscaling
    def upscale():
        new_grid = [[0 for i in range(2*len(grid[0])-1)]
                    for j in range(2*len(grid)-1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) in vis:
                    new_grid[2*i][2*j] = 1
        vis = set()

        def dfs(row, col):
            for r, c in zip([0, 0, 1, -1], [1, -1, 0, 0]):
                new_row = r + row
                new_col = c + col
                if 0 <= new_row < len(new_grid) and 0 <= new_col < len(new_grid[0]) and new_grid[new_row][new_col] == 0 and (new_row, new_col) not in vis:
                    vis.add((new_row, new_col))
                    dfs(new_row, new_col)
        for i in range(len(new_grid)):
            for j in range(len(new_grid[0])):
                if i == 0 or j == 0 or i == len(new_grid)-1 or j == len(new_grid[0])-1 and new_grid[i][j] == 0 and (i, j) not in vis:
                    vis.add((i, j))
                    dfs(i, j)
        count = 0
        print(vis)
        print(new_grid[12], (12, 4) in vis)
        print(new_grid[14])
        for i in range(len(new_grid)):
            for j in range(len(new_grid[0])):
                # print(new_grid[i])
                if i % 2 == 0 and j % 2 == 0 and new_grid[i][j] == 0:
                    if (i, j) not in vis:
                        # print(grid[i//2], grid[i//2][j//2])
                        grid[i//2][j//2] = 0
                        # print(grid[i//2], grid[i//2][j//2])
                        count += 1
        for i in grid:
            print(i)
        return count

    # Tried row by row iterate
    def iterate():
        def satisfy(i, j, j1):
            if grid[i][j] == '|' == grid[i][j1]:
                return True
            if grid[i][j] == '7' and grid[i][j1] in ['F', '|']:
                return True
            if grid[i][j] == 'J' and grid[i][j1] in ['L', '|']:
                return True
            if grid[i][j] == '|' and grid[i][j1] in ['F', 'L']:
                return True
            return False
        for i in range(len(grid)):
            count = 0
            for j in range(len(grid[0])):
                if (i, j) not in vis and count % 2 == 1:
                    ans += 1
                if (i, j) in vis:
                    if count % 2 == 0 and (j > 0 and (grid[i][j-1] == "." or satisfy(i, j-1, j))):
                        count += 1
                    elif count % 2 == 1 and (j < len(grid[0])-1 and (grid[i][j+1] == "." or satisfy(i, j, j+1))):
                        count += 1
            print(grid[i], count, ans)
        return ans

    # Using Shoelace formula
    for i in range(len(vislist)):
        next = (i+1) % len(vislist)
        prev = (i-1) % len(vislist)
        ans += vislist[i][0]*(vislist[next][1]-vislist[prev][1])
    # Using picks theorem
    return abs(ans//2) + 1 - len(vislist)//2


if __name__ == "__main__":
    print(f"Answer for part one: {part1()}")
    print(f"Answer for part two: {part2()}")
