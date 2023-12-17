import heapq

f = open("day17.txt", "r")
data = f.readlines()
f.close()

moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # [d, r, u, l]
count = 0
grid = []
for line in data:
    line = line.strip()
    grid.append(list(line))

def check(dirs):
    total = 0
    row = 0
    col = 0
    for dir in dirs:
        dir = int(dir)
        row += moves[dir][0]
        col += moves[dir][1]
        total += int(grid[row][col])
    return total

def part1():
    def search():
        while pq:
            # nonlocal count
            # count += 1
            # if count >= 1000000:
            #     # print(pq)
            #     return
            # print(pq)
            heat, row, col, dirs = heapq.heappop(pq)
            if row == len(grid)-1 and col == len(grid[0])-1:
                # print(pq)
                return heat, dirs, len(dirs)
            ignore = set()
            if dirs:
                ignore.add((int(dirs[-1])+2) % 4)
                if len(dirs) >= 3 and len(set(dirs[-3:])) == 1:
                    ignore.add(int(dirs[-1]))
            for move in range(len(moves)):
                if move not in ignore:
                    nrow = row + moves[move][0]
                    ncol = col + moves[move][1]
                    if 0 <= nrow < len(grid) and 0 <= ncol < len(grid[0]):
                        # ndirs = dirs[1:]
                        ndirs = dirs
                        ndirs += str(move)
                        newmove = (
                            heat+int(grid[nrow][ncol]), nrow, ncol, ndirs)
                        if (nrow, ncol, ndirs[-3:]) not in vis:
                            heapq.heappush(pq, newmove)
                            vis.add((nrow, ncol, ndirs[-3:]))
        return -1, -1, -1

    pq = []
    vis = {(0, 0, "")}
    heapq.heappush(pq, (0, 0, 0, ""))
    return search()[0]


def part2():
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # [d, r, u, l]

    def search():
        while pq:
            heat, row, col, dirs = heapq.heappop(pq)
            if row == len(grid)-1 and col == len(grid[0])-1 and len(set(dirs[-4:])) == 1:
                # print(pq)
                return heat, dirs, len(dirs)
            if 0 < len(dirs) < 4 or len(set(dirs[-4:])) > 1:
                move = int(dirs[-1])
                nrow = row + moves[move][0]
                ncol = col + moves[move][1]
                if 0 <= nrow < len(grid) and 0 <= ncol < len(grid[0]):
                    dirs += dirs[-1]
                    newmove = (heat+int(grid[nrow][ncol]), nrow, ncol, dirs)
                    if (nrow, ncol, dirs[-10:]) not in vis:
                        heapq.heappush(pq, newmove)
                        vis.add((nrow, ncol, dirs[-10:]))
            else:
                ignore = set()
                if dirs:
                    ignore.add((int(dirs[-1])+2) % 4)
                    if len(dirs) >= 10 and len(set(dirs[-10:])) == 1:
                        ignore.add(int(dirs[-1]))

                for move in range(len(moves)):
                    if move not in ignore:
                        nrow = row + moves[move][0]
                        ncol = col + moves[move][1]
                        if 0 <= nrow < len(grid) and 0 <= ncol < len(grid[0]):
                            # ndirs = dirs[1:]
                            ndirs = dirs
                            ndirs += str(move)
                            newmove = (
                                heat+int(grid[nrow][ncol]), nrow, ncol, ndirs)
                            if (nrow, ncol, ndirs[-10:]) not in vis:
                                heapq.heappush(pq, newmove)
                                vis.add((nrow, ncol, ndirs[-10:]))
        return -1, -1, -1

    pq = []
    vis = {(0, 0, "")}
    heapq.heappush(pq, (0, 0, 0, ""))
    return search()[0]

if __name__ == "__main__":
    print(f"Answer for part one: {part1()}")
    print(f"Answer for part two: {part2()}")
