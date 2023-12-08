from math import gcd

f = open("day8.txt", "r")
data = f.readlines()
f.close()


def part1():
    tree = dict()
    steps = data[0].strip()
    for i in range(2, len(data)):
        line = data[i].strip()
        start, dirs = line.split(" = ")
        dirs = dirs[1:-1].split(", ")
        tree[start] = dirs
    curr = "AAA"
    count = 0
    # print(tree)
    while curr != "ZZZ":
        for step in steps:
            # print(count, curr, step)
            if curr == "ZZZ":
                return count
            if step == "L":
                curr = tree[curr][0]
            else:
                curr = tree[curr][1]
            count += 1
        if curr == "AAA":
            return -1
    return count


def part2():
    tree = dict()
    steps = data[0].strip()
    for i in range(2, len(data)):
        line = data[i].strip()
        start, dirs = line.split(" = ")
        dirs = dirs[1:-1].split(", ")
        tree[start] = dirs
    values = []
    for node in tree:
        if node.endswith("A"):
            curr = node
            count = 0
            # print(tree)
            found = False
            while not found and not curr.endswith("Z"):
                for step in steps:
                    # print(count, curr, step)
                    if curr.endswith("Z"):
                        values.append(count)
                        found = True
                    if not found:
                        if step == "L":
                            curr = tree[curr][0]
                        else:
                            curr = tree[curr][1]
                        count += 1
                        if curr.endswith("A"):
                            return -1
            if not found:
                values.append(count)
    lcm = 1
    for i in values:
        lcm = lcm*i//gcd(lcm, i)
    return lcm


if __name__ == "__main__":
    print(f"Answer for part one: {part1()}")
    print(f"Answer for part two: {part2()}")
