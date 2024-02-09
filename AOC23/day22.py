from collections import defaultdict
import heapq

f = open("day22.txt", "r")
data = f.readlines()
f.close()


def orientation(brick):
    print((brick[1], brick[2], brick[0]), (brick[4], brick[5], brick[3]))
    if brick[0] != brick[3]:
        return brick[0], brick[3]+1, 2
    elif brick[1] != brick[4]:
        return brick[1], brick[4]+1, 0
    return brick[2], brick[5]+1, 1


def count(idx, graph, n):
    indeg = [0 for __ in range(n)]
    for j in range(n):
        for i in graph[j]:
            indeg[i] += 1
    q = [idx]
    count = -1
    while len(q) > 0:
        count += 1
        x = q.pop()
        for i in graph[x]:
            indeg[i] -= 1
            if indeg[i] == 0:
                q.append(i)

    return count


bricks = []
# brickheap = []
# heapq.heapify(brickheap)
for line in data:
    start, end = line.strip().split('~')
    start = list(map(int, start.split(',')))
    end = list(map(int, end.split(',')))
    if start[2] > end[2]:
        start, end = end, start
    # brick = (start[2], start[0], start[1], end[2], end[0], end[1])
    # heapq.heappush(brickheap, brick)
    bricks.append((start, end))
graph = [[] for i in range(len(bricks))]


def part1():

    # occupied = set()
    # brick_no = 0
    # brick_base = defaultdict(int)
    # brick_base_flip = defaultdict(list)
    # brick_top = defaultdict(int)
    # brick_top_flip = defaultdict(list)
    # top_max = 1
    # while brickheap:
    #     print(f"###########{brick_no}##########")
    #     brick = heapq.heappop(brickheap)
    #     # print(brick)
    #     base = top_max
    #     start, end, orient = orientation(brick)
    #     init = [brick[1], brick[2], brick[0]]
    #     while True:
    #         # print(occupied)
    #         clash = False
    #         for a in range(start, end):
    #             new = init[:]
    #             new[orient] = a
    #             if orient != 2:
    #                 new[2] = base
    #             else:
    #                 new[2] += base - init[2]
    #             # print("checking", new)
    #             if tuple(new) in occupied:
    #                 # print("clash")
    #                 clash = True
    #                 break
    #         if clash or base == 0:
    #             base += 1
    #             print(base)
    #             break
    #         base -= 1
    #     # print(base)
    #     top = base + 1
    #     for a in range(start, end):
    #         new = init[:]
    #         new[orient] = a
    #         # print("new", new)
    #         if orient != 2:
    #             new[2] = base
    #         else:
    #             new[2] += base - init[2]
    #         if new[2] + 1 > top:
    #             top = new[2] + 1
    #         # print(new)
    #         occupied.add(tuple(new))
    #     brick_top[brick_no] = top
    #     brick_base[brick_no] = base
    #     brick_top_flip[top].append(brick_no)
    #     brick_base_flip[base].append(brick_no)
    #     # print(top)
    #     top_max = max(top, top_max)
    #     brick_no += 1
    # # print(brick_base, brick_top, sep='\n')
    # brick_supporting = defaultdict(list)
    # brick_supported = defaultdict(list)
    # for brick in range(brick_no):
    #     top = brick_top[brick]
    #     brick_supporting[brick].extend(brick_base_flip[top])
    #     base = brick_base[brick]
    #     brick_supported[brick].extend(brick_top_flip[base])
    # print("brick is supporting", brick_supporting)
    # print("brick is supported by", brick_supported)
    # need = set()
    # for brick in range(brick_no):
    #     supporting = brick_supporting[brick]
    #     for new_brick in supporting:
    #         if len(brick_supported[new_brick]) == 1:
    #             need.add(brick)
    # return brick_no - len(need)
    n = len(bricks)

    bricks.sort(key=lambda x: x[0][2])

    highest = defaultdict(lambda: (0, -1))
    bad = set()
    for idx, b in enumerate(bricks):
        mxh = -1
        support_set = set()
        for x in range(b[0][0], b[1][0]+1):
            for y in range(b[0][1], b[1][1]+1):
                if highest[x, y][0] + 1 > mxh:
                    mxh = highest[x, y][0] + 1
                    support_set = {highest[x, y][1]}
                elif highest[x, y][0] + 1 == mxh:
                    support_set.add(highest[x, y][1])

        for x in support_set:
            if x != -1:
                graph[x].append(idx)

        if len(support_set) == 1:
            bad.add(support_set.pop())

        fall = b[0][2] - mxh
        if fall > 0:
            b[0][2] -= fall
            b[1][2] -= fall

        for x in range(b[0][0], b[1][0]+1):
            for y in range(b[0][1], b[1][1]+1):
                highest[x, y] = (b[1][2], idx)

    return len(bricks)-len(bad)+1


def part2():
    return sum(count(x, graph, len(bricks)) for x in range(len(bricks)))


if __name__ == "__main__":
    print(f"Answer for part one: {part1()}")
    print(f"Answer for part two: {part2()}")
