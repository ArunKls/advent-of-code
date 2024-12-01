from collections import defaultdict

f = open("day1.txt", "r")
data = f.readlines()
f.close()

def part1():
    list1 = []
    list2 = []
    ans = 0
    for line in data:
        x, y = line.split()
        list1.append(int(x))
        list2.append(int(y))
    list1.sort()
    list2.sort()
    for x, y in zip(list1, list2):
        ans += abs(x-y)
    return ans

def part2():
    ddict = defaultdict(int)
    list1 = []
    ans = 0
    for line in data:
        x, y = line.split()
        list1.append(int(x))
        ddict[int(y)] += 1
    for i in list1:
        ans += i * ddict[i]
    return ans

if __name__ == "__main__":
    print(f"Answer for part one: {part1()}")
    print(f"Answer for part two: {part2()}")

