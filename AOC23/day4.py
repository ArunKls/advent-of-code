

f = open("day4.txt", "r")
data = f.readlines()
f.close()


def part1():
    ans = 0
    for line in data:
        line = line.strip().split(": ")[-1]
        winning, have = line.split(" | ")
        winning = set(winning.split())
        have = have.split()
        count = 0
        for card in have:
            if card in winning:
                count += 1
        if count:
            ans += (2**(count-1))
    return ans


def part2():
    counts = []
    for line in data:
        line = line.strip().split(": ")[-1]
        winning, have = line.split(" | ")
        winning = set(winning.split())
        have = have.split()
        count = 0
        for card in have:
            if card in winning:
                count += 1
        counts.append(count)
    card_counts = [1 for i in range(len(counts))]
    total = 0
    for i in range(len(counts)):
        for j in range(i+1, i+counts[i]+1):
            card_counts[j] += card_counts[i]
        total += card_counts[i]
    return total


if __name__ == "__main__":
    print(f"Answer for part one: {part1()}")
    print(f"Answer for part two: {part2()}")
