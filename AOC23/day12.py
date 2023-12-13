

f = open("day12.txt", "r")
data = f.readlines()
f.close()


def ways(pattern, numbers):
    ans = []
    # print(pattern, numbers)

    def helper(pattern_idx, num_idx, curr, pattern):
        # print(pattern_idx, num_idx, curr)
        if pattern_idx == len(pattern) and num_idx == len(numbers):
            if curr == 0:
                # print("pattern found")
                ans.append(1)
                return
        if num_idx >= len(numbers):
            if pattern[pattern_idx] == '.':
                return helper(pattern_idx+1, num_idx, curr, pattern[:])
            if pattern[pattern_idx] == '?':
                return helper(pattern_idx+1, num_idx, 0, pattern[:])

        if num_idx >= len(numbers):
            return

        if curr == numbers[num_idx]:
            if num_idx < len(numbers):
                return helper(pattern_idx, num_idx+1, 0, pattern[:])
            return
        if curr > numbers[num_idx]:
            return
        if pattern_idx >= len(pattern):
            return
        if pattern[pattern_idx] != '?':
            if pattern[pattern_idx] == '.':
                if curr == numbers[num_idx]:
                    return helper(pattern_idx+1, num_idx+1, 0, pattern[:])
                if curr == 0:
                    return helper(pattern_idx+1, num_idx, curr, pattern[:])
                return
            elif pattern[pattern_idx] == '#':
                if curr == 0:
                    if pattern_idx == 0 or (pattern_idx > 0 and pattern[pattern_idx-1] != '#'):
                        return helper(pattern_idx+1, num_idx, curr+1, pattern[:])
                    return
                return helper(pattern_idx+1, num_idx, curr+1, pattern[:])
        else:
            new_pattern = pattern[:]
            if curr == 0:
                if pattern_idx == 0 or (pattern_idx > 0 and pattern[pattern_idx-1] != '#'):
                    new_pattern[pattern_idx] = '#'
                    # print('? found, put #')
                    helper(pattern_idx+1, num_idx, curr+1, new_pattern)
                new_pattern[pattern_idx] = '.'
                # print('? found, put .')
                helper(pattern_idx+1, num_idx, 0, new_pattern)
                return
            else:
                new_pattern[pattern_idx] = '#'
                # print('? found, put #')
                helper(pattern_idx+1, num_idx, curr+1, new_pattern)
                if curr == numbers[num_idx]:
                    new_pattern[pattern_idx] = '.'
                    # print('? found, put .')
                    helper(pattern_idx+1, num_idx+1, 0, new_pattern)
                return
    helper(0, 0, 0, pattern)
    return len(ans)


def part1():
    ans = 0
    for line in data:
        line = line.strip()
        pattern, numbers = line.split()
        numbers = numbers.split(",")
        permutations = ways(list(pattern), [int(i) for i in numbers])
        ans += permutations
    return ans


def part2():
    ans = 0
    for line in data:
        line = line.strip()
        pattern, numbers = line.split()
        numbers = numbers.split(",")
        patternlist = [pattern for i in range(5)]
        patternlist = '?'.join(patternlist)
        numbers = [int(i) for i in numbers]
        numberslist = []
        for i in range(5):
            numberslist.extend(numbers)
        permutations = ways(list(patternlist), numberslist)
        ans += permutations
    return ans


if __name__ == "__main__":
    print(f"Answer for part one: {part1()}")
    print(f"Answer for part two: {part2()}")
