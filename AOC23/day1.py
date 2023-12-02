

f = open("day1.txt", "r")
data = f.readlines()
f.close()


def part1():
    ans = 0
    for line in data:
        line = line.strip()
        num = 0
        for i in range(len(line)):
            if 48 <= ord(line[i]) <= 57:
                num = num*10 + int(line[i])
                break
        for i in range(len(line)-1, -1, -1):
            if 48 <= ord(line[i]) <= 57:
                num = num*10 + int(line[i])
                break
        ans += num
    return ans


def part2():
    lps_dict = dict()
    patterns = ["one", "two", "three", "four", "five",
                "six", "seven", "eight", "nine", "ten"]

    def computeLPS():
        for idx, pattern in enumerate(patterns):
            lps = [0]*len(pattern)
            length = 0
            lps[0] = 0
            i = 1
            while i < len(pattern):
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length-1]
                    else:
                        lps[i] = 0
                        i += 1
            lps_dict[idx+1] = lps[:]

    def search(pattern, num, text):
        i, j = 0, 0
        M, N = len(pattern), len(text)
        idxs = []
        while N - i >= M - j:
            if pattern[j] == text[i]:
                i += 1
                j += 1

            if j == M:
                idxs.append(i-j)
                j = lps_dict[num][j-1]

            elif i < N and pattern[j] != text[i]:
                if j != 0:
                    j = lps_dict[num][j-1]
                else:
                    i += 1
        return idxs

    computeLPS()
    ans = 0
    for line in data:
        line = line.strip()
        min_idx = len(line)
        min_str = None
        max_idx = -1
        max_str = None
        for i in range(len(line)):
            if 48 <= ord(line[i]) <= 57:
                min_idx = i
                min_str = int(line[i])
                break
        for i in range(len(line)-1, -1, -1):
            if 48 <= ord(line[i]) <= 57:
                max_idx = i
                max_str = int(line[i])
                break
        for num, pattern in enumerate(patterns):
            idxs = search(pattern, num+1, line)
            if idxs and idxs[0] < min_idx:
                min_idx = idxs[0]
                min_str = num+1
            if idxs and idxs[-1] > max_idx:
                max_idx = idxs[-1]
                max_str = num+1
        val = min_str*10 + max_str
        ans += val
        # print(val)
    return ans


if __name__ == "__main__":
    print(f"Answer for part one: {part1()}")
    print(f"Answer for part two: {part2()}")
