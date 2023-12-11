

f = open("day11.txt", "r")
data = f.readlines()
f.close()

points = []
emp_rows = set()
emp_cols = set()
grid = []
for i, line in enumerate(data):
    line = list(line.strip())
    count = 0
    for j, point in enumerate(line):
        if point=='#':
            points.append((i, j))
            count += 1
    if not count:
        emp_rows.add(i)
    grid.append(line[:])
for j in range(len(grid[0])):
    count = 0
    for i in range(len(grid)):
        if grid[i][j] == '#':
            count += 1
    if not count:
        emp_cols.add(j)
# for i in grid:
#     print(i)
# print(emp_rows, emp_cols, points)
emp_rows_map = [0 for i in range(len(grid))]
emp_cols_map = [0 for i in range(len(grid[0]))]
for i, row in enumerate(emp_rows):
    emp_rows_map[row] = 1
for i, col in enumerate(emp_cols):
    emp_cols_map[col] = 1
for i in range(1, len(emp_rows_map)):
    emp_rows_map[i] += emp_rows_map[i-1]
for i in range(1, len(emp_cols_map)):
    emp_cols_map[i] += emp_cols_map[i-1]

def part1():
    total = 0
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            dist = abs(points[i][0] - abs(points[j][0])) + abs(points[i][1]-points[j][1])
            dist += abs(emp_rows_map[points[j][0]] - emp_rows_map[points[i][0]])
            dist += abs(emp_cols_map[points[j][1]] - emp_cols_map[points[i][1]])
            total += dist
    return total

def part2():
    total = 0
    factor = 999999
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            dist = abs(points[i][0] - abs(points[j][0])) + abs(points[i][1]-points[j][1])
            dist += factor*(abs(emp_rows_map[points[j][0]] - emp_rows_map[points[i][0]]))
            dist += factor*(abs(emp_cols_map[points[j][1]] - emp_cols_map[points[i][1]]))
            total += dist
    return total

if __name__ == "__main__":
    print(f"Answer for part one: {part1()}")
    print(f"Answer for part two: {part2()}")

