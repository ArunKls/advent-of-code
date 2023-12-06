import math

f = open("day6.txt", "r")
data = f.readlines()
f.close()


def part1():
    time = data[0].strip()
    times = (time.split(":")[-1]).strip()
    times = times.split()
    distance = data[1].strip()
    distances = (distance.split(":")[-1]).strip()
    distances = distances.split()
    ans = 1
    for t, d in zip(times, distances):
        t, d = int(t), int(d)
        # equation: x^2 -tx + d <= 0
        val = math.sqrt(t**2 - 4*d)
        root1 = (t-val)/2
        root2 = (t+val)/2
        if root1 % 1 != 0:
            root1 = math.ceil(root1)
        else:
            root1 += 1
        if root2 % 1 != 0:
            root2 = math.ceil(root2)
        ans *= int(root2-root1)
    return ans


def part2():
    time = data[0].strip()
    times = (time.split(":")[-1]).strip()
    times = times.split()
    distance = data[1].strip()
    distances = (distance.split(":")[-1]).strip()
    distances = distances.split()
    t = int(''.join(times))
    d = int(''.join(distances))
    val = math.sqrt(t**2 - 4*d)
    root1 = (t-val)/2
    root2 = (t+val)/2
    if root1 % 1 != 0:
        root1 = math.ceil(root1)
    else:
        root1 += 1
    if root2 % 1 != 0:
        root2 = math.ceil(root2)
    return int(root2-root1)


if __name__ == "__main__":
    print(f"Answer for part one: {part1()}")
    print(f"Answer for part two: {part2()}")
