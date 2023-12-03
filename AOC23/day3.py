

f = open("day3.txt", "r")
data = f.readlines()
f.close()


def part1():
    visited = set()
    total = []
    M, N = len(data), len(data[0].strip())

    def dfs(row, col, visited):
        rows = [1, -1, 0, 0, 1, 1, -1, -1]
        cols = [0, 0, 1, -1, 1, -1, 1, -1]
        for move in range(8):
            nrow = row + rows[move]
            ncol = col + cols[move]
            if 0 <= nrow < M and 0 <= ncol < N and (nrow, ncol) not in visited:
                if 48 <= ord(data[nrow][ncol]) <= 57:
                    number = data[nrow][ncol]
                    # print(row, col, nrow, ncol, number)
                    visited.add((nrow, ncol))
                    curr = ncol - 1
                    while curr >= 0 and 48 <= ord(data[nrow][curr]) <= 57:
                        number = data[nrow][curr] + number
                        visited.add((nrow, curr))
                        curr -= 1
                    curr = ncol + 1
                    while curr < N and 48 <= ord(data[nrow][curr]) <= 57:
                        number = number + data[nrow][curr]
                        visited.add((nrow, curr))
                        curr += 1
                    # print(number)
                    total.append(int(number))

    for i, line in enumerate(data):
        for j, cell in enumerate(line.strip()):
            if cell != "." and not (48 <= ord(cell) <= 57):
                # print(cell, ord(cell), "symbol", i, j)
                visited.add((i, j))
                dfs(i, j, visited)
    return sum(total)


def part2():
    visited = set()
    total = []
    M, N = len(data), len(data[0].strip())

    def dfs(row, col, visited):
        rows = [1, -1, 0, 0, 1, 1, -1, -1]
        cols = [0, 0, 1, -1, 1, -1, 1, -1]
        curr_total = []
        for move in range(8):
            nrow = row + rows[move]
            ncol = col + cols[move]
            if len(curr_total) < 2 and 0 <= nrow < M and 0 <= ncol < N and (nrow, ncol) not in visited:
                if 48 <= ord(data[nrow][ncol]) <= 57:
                    number = data[nrow][ncol]
                    # print(row, col, nrow, ncol, number)
                    visited.add((nrow, ncol))
                    curr = ncol - 1
                    while curr >= 0 and 48 <= ord(data[nrow][curr]) <= 57:
                        number = data[nrow][curr] + number
                        visited.add((nrow, curr))
                        curr -= 1
                    curr = ncol + 1
                    while curr < N and 48 <= ord(data[nrow][curr]) <= 57:
                        number = number + data[nrow][curr]
                        visited.add((nrow, curr))
                        curr += 1
                    # print(number)
                    curr_total.append(int(number))
        if len(curr_total) == 2:
            total.append(curr_total[0]*curr_total[1])

    for i, line in enumerate(data):
        for j, cell in enumerate(line.strip()):
            if cell == "*":
                # print(cell, ord(cell), "symbol", i, j)
                visited.add((i, j))
                dfs(i, j, visited)
    return sum(total)


if __name__ == "__main__":
    print(f"Answer for part one: {part1()}")
    print(f"Answer for part two: {part2()}")
