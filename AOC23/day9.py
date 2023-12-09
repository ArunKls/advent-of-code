

f = open("day9.txt", "r")
data = f.readlines()
f.close()


def part1():
    def next_pattern(tc):
        i = 0
        total = tc[-1]
        # print(tc, total)
        while len(set(tc[i:])) != 1 and i < len(tc):
            for j in range(len(tc)-1, i, -1):
                # print(tc[j], tc[j-1])
                tc[j] -= tc[j-1]
            i += 1
            total += tc[-1]
            # print(tc, total)
        # print(tc[i:])
        return total

    total = 0
    for line in data:
        line = (line.strip()).split()
        tc = []
        for number in line:
            tc.append(int(number))
        total += next_pattern(tc[:])
    return total


def part2():
    def next_pattern(tc):
        i = len(tc)
        total = tc[0]
        # print(tc, total)
        k = 1
        while len(set(tc[:i])) != 1 and i >= 0:
            for j in range(1, i):
                # print(tc[j], tc[j-1])
                tc[j-1] = tc[j] - tc[j-1]
            i -= 1
            add = tc[0]
            if k % 2 != 0:
                add *= -1
            total += add
            k += 1
            # print(tc, total)
        return total

    total = 0
    for line in data:
        line = (line.strip()).split()
        tc = []
        for number in line:
            tc.append(int(number))
        total += next_pattern(tc[:])
    return total


if __name__ == "__main__":
    print(f"Answer for part one: {part1()}")
    print(f"Answer for part two: {part2()}")
