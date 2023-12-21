from collections import deque
from copy import deepcopy
from math import ceil

f = open("day21.txt", "r")
data = f.readlines()
f.close()

grid = []
q = deque()
for i, line in enumerate(data):
    line = list(line.strip())
    grid.append(line)
    for j, char in enumerate(line):
        if char == 'S':
            start = (i, j)


def part1():
    q.append(start)

    def bfs():
        count = 0
        while q:
            count += 1
            lenq = len(q)
            for state in range(lenq):
                r, c = q.popleft()
                rs = [1, -1, 0, 0]
                cs = [0, 0, 1, -1]
                for i in range(4):
                    nr, nc = r + rs[i], c + cs[i]
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != '#' and (nr, nc) not in q:
                        q.append((nr, nc))
            # print(count, len(q))
            if count == 64:
                return len(q)
    bfs()

# From xoronths solution
def part2():
    lines = deepcopy(grid)
    height = len(lines)
    width = len(lines[0])
    mod = 26501365 % height

    seen_states = []

    for run in [mod, mod + height, mod + height * 2]:
        next_queue = [start]
        for _ in range(run):
            curr_queue = deepcopy(next_queue)
            visited = set(deepcopy(next_queue))
            next_queue = []

            while curr_queue:
                curr = curr_queue.pop(0)

                for dir in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    new_y, new_x = curr[0] + dir[0], curr[1] + dir[1]

                    if (
                        lines[new_y % height][new_x % width] != "#"
                        and (new_y, new_x) not in visited
                    ):
                        visited.add((new_y, new_x))
                        next_queue.append((new_y, new_x))

        seen_states.append(len(next_queue))

    # seen_states = [3835, 34125, 94603] # hard-coded after running above since it's slow...
    print(seen_states)
    m = seen_states[1] - seen_states[0]
    n = seen_states[2] - seen_states[1]
    a = (n - m) // 2
    b = m - 3 * a
    c = seen_states[0] - b - a

    ceiling = ceil(26501365 / height)

    answer = a * ceiling**2 + b * ceiling + c

    return answer


if __name__ == "__main__":
    print(f"Answer for part one: {part1()}")
    print(f"Answer for part two: {part2()}")
