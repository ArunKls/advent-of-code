

f = open("day13.txt", "r")
data = f.readlines()
f.close()


def check(pattern, smudges=0):
    for i, line in enumerate(pattern):
        if i + 1 == len(pattern):
            return 0
        pairs_to_check = [
            (c1, c2)
            for line1, line2 in zip(pattern[i::-1], pattern[i+1:])
            for c1, c2 in zip(line1, line2)
        ]
        if sum(
            1 for c1, c2 in pairs_to_check if c1 == c2
        ) == len(pairs_to_check) - smudges:
            return i + 1


def part1():
    grids = []
    gridsT = []
    grid = []
    for line in data:
        line = line.strip()
        if not line:
            grids.append(grid[:])
            grid = []
        else:
            grid.append(line)
    grids.append(grid[:])
    for grid in grids:
        gridsT.append(list(zip(*grid)))

    ans = 0
    for grid in grids:
        rcheck = check(grid)
        ans += 100*rcheck
    if not rcheck:
        for gridT in gridsT:
            ans += check(gridT)
    return ans


def part2():
    grids = []
    gridsT = []
    grid = []
    for line in data:
        line = line.strip()
        if not line:
            grids.append(grid[:])
            grid = []
        else:
            grid.append(line)
    grids.append(grid[:])
    for grid in grids:
        gridsT.append(list(zip(*grid)))

    ans = 0
    for grid in grids:
        rcheck = check(grid, 1)
        ans += 100*rcheck
    if not rcheck:
        for gridT in gridsT:
            ans += check(gridT, 1)
    return ans


if __name__ == "__main__":
    print(f"Answer for part one: {part1()}")
    print(f"Answer for part two: {part2()}")
