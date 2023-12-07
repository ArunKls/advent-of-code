from functools import cmp_to_key
from collections import Counter

f = open("day7.txt", "r")
data = f.readlines()
f.close()


def part1():
    def kind(hand):
        counts = Counter(list(hand))
        if len(counts) == 1:
            return 5
        values = list(counts.values())
        if len(counts) == 2 and 4 in values:
            return 4
        if len(counts) == 2 and 3 in values:
            return 3
        if len(counts) == 3 and 3 in values:
            return 2
        if len(counts) == 3 and values.count(2) == 2:
            return 1
        if len(counts) == 4:
            return 0
        return -1

    def compare(hand1, hand2):
        cards = ["A", "K", "Q", "J", "T", "9",
                 "8", "7", "6", "5", "4", "3", "2"]
        hand1, hand2 = hand1[0], hand2[0]
        kind1 = kind(hand1)
        kind2 = kind(hand2)
        if kind1 < kind2:
            return -1
        if kind1 > kind2:
            return 1
        for card1, card2 in zip(hand1, hand2):
            if card1 == card2:
                continue
            if cards.index(card1) > cards.index(card2):
                return -1
            if cards.index(card1) < cards.index(card2):
                return 1
        return 0

    input = []
    for line in data:
        line = line.strip()
        hand, bid = line.split()
        input.append((hand, int(bid)))
    # print(input)
    input.sort(key=cmp_to_key(compare))
    # print(input)
    ans = 0
    for i, elem in enumerate(input):
        ans += (i+1)*elem[1]
    return ans


def part2():
    def kind(hand):
        counts = Counter(list(hand))
        if len(counts) == 1:
            return 5
        if "J" in counts:
            jcount = counts.pop("J")
            keys = list(counts.keys())
            keys.sort(key=lambda x: counts[x])
            counts[keys[-1]] += jcount
            # print(hand, counts)
        if len(counts) == 1:
            return 5
        values = list(counts.values())
        if len(counts) == 2 and 4 in values:
            return 4
        if len(counts) == 2 and 3 in values:
            return 3
        if len(counts) == 3 and 3 in values:
            return 2
        if len(counts) == 3 and values.count(2) == 2:
            return 1
        if len(counts) == 4:
            return 0
        return -1

    def compare(hand1, hand2):
        cards = ["A", "K", "Q", "T", "9", "8",
                 "7", "6", "5", "4", "3", "2", "J"]
        hand1, hand2 = hand1[0], hand2[0]
        kind1 = kind(hand1)
        kind2 = kind(hand2)
        if kind1 < kind2:
            return -1
        if kind1 > kind2:
            return 1
        for card1, card2 in zip(hand1, hand2):
            if card1 == card2:
                continue
            if cards.index(card1) > cards.index(card2):
                return -1
            if cards.index(card1) < cards.index(card2):
                return 1
        return 0

    input = []
    for line in data:
        line = line.strip()
        hand, bid = line.split()
        input.append((hand, int(bid)))
    # print(input)
    input.sort(key=cmp_to_key(compare))
    # print(input)
    ans = 0
    for i, elem in enumerate(input):
        ans += (i+1)*elem[1]
    return ans


if __name__ == "__main__":
    print(f"Answer for part one: {part1()}")
    print(f"Answer for part two: {part2()}")
