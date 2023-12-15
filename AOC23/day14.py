import matplotlib.pyplot as plt
import numpy

f = open("day14.txt", "r")
data = f.readlines()
f.close()


def move(data):
    counts = []
    for idx in range(len(data[0])):
        cts = []
        ct = 0
        for jdx in range(len(data)):
            if data[jdx][idx] == 'O':
                ct += 1
                data[jdx][idx] = '.'
            elif data[jdx][idx] == '#':
                cts.append(ct)
                ct = 0
        cts.append(ct)
        counts.append(cts[::-1])
    for idx in range(len(data[0])):
        i = -1
        for jdx in range(len(data)):
            if data[jdx][idx] == "#":
                i -= 1
            elif counts[idx][i] > 0:
                # print(len(data)-jdx)
                data[jdx][idx] = 'O'
                counts[idx][i] -= 1
    # for line in data:
    #     print(line)
    # print('\n')
    counts = []
    for idx in range(len(data)):
        cts = []
        ct = 0
        for jdx in range(len(data[0])):
            if data[idx][jdx] == 'O':
                ct += 1
                data[idx][jdx] = '.'
            elif data[idx][jdx] == '#':
                cts.append(ct)
                ct = 0
        cts.append(ct)
        counts.append(cts[::-1])
    for idx in range(len(data)):
        i = -1
        for jdx in range(len(data[0])):
            if data[idx][jdx] == "#":
                i -= 1
            elif counts[idx][i] > 0:
                # print(len(data)-jdx)
                data[idx][jdx] = 'O'
                counts[idx][i] -= 1
    # for line in data:
    #     print(line)
    # print('\n')
    counts = []
    for idx in range(len(data[0])):
        cts = []
        ct = 0
        for jdx in range(len(data)-1, -1, -1):
            if data[jdx][idx] == 'O':
                ct += 1
                data[jdx][idx] = '.'
            elif data[jdx][idx] == '#':
                cts.append(ct)
                ct = 0
        cts.append(ct)
        counts.append(cts[::-1])
    for idx in range(len(data[0])):
        i = -1
        for jdx in range(len(data)-1, -1, -1):
            if data[jdx][idx] == "#":
                i -= 1
            elif counts[idx][i] > 0:
                # print(len(data)-jdx)
                data[jdx][idx] = 'O'
                counts[idx][i] -= 1
    # for line in data:
    #     print(line)
    # print('\n')
    counts = []
    for idx in range(len(data)):
        cts = []
        ct = 0
        for jdx in range(len(data[0])-1, -1, -1):
            if data[idx][jdx] == 'O':
                ct += 1
                data[idx][jdx] = '.'
            elif data[idx][jdx] == '#':
                cts.append(ct)
                ct = 0
        cts.append(ct)
        counts.append(cts[::-1])
    for idx in range(len(data)):
        i = -1
        for jdx in range(len(data[0])-1, -1, -1):
            if data[idx][jdx] == "#":
                i -= 1
            elif counts[idx][i] > 0:
                # print(len(data)-jdx)
                data[idx][jdx] = 'O'
                counts[idx][i] -= 1

    total = 0
    for i, line in enumerate(data):
        count = 0
        for char in line:
            if char == 'O':
                count += 1
        total += (len(data)-i)*count
    return data, total


def part1():
    counts = []
    for idx in range(len(data[0].strip())):
        cts = []
        ct = 0
        for jdx, line in enumerate(data):
            line = line.strip()
            if line[idx] == 'O':
                ct += 1
            elif line[idx] == '#':
                cts.append(ct)
                ct = 0
        cts.append(ct)
        counts.append(cts[::-1])
    total = 0
    for idx in range(len(data[0].strip())):
        i = -1
        for jdx, line in enumerate(data):
            if line[idx] == "#":
                i -= 1
            elif counts[idx][i] > 0:
                # print(len(data)-jdx)
                total += len(data)-jdx
                counts[idx][i] -= 1

    return total


def part2():
    grid = []
    for line in data:
        line = line.strip()
        grid.append(list(line))
    vals = []
    scores = []
    check = 1000000000
    check = check%77
    for i in range(check+770):
        grid, score = move(grid)
    return score

    # print(vals, scores)

    # fig = plt.figure()
    # ax = fig.gca()
    # ax.set_xticks(numpy.arange(800, 1000, 10))
    # ax.set_yticks(numpy.arange(80000, 90000, 10))
    # ax.grid()
    # ax.set_axisbelow(True)
    # plt.plot(vals, scores)
    # plt.show()


if __name__ == "__main__":
    print(f"Answer for part one: {part1()}")
    print(f"Answer for part two: {part2()}")
