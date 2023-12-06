

f = open("day5.txt", "r")
data = f.readlines()
f.close()


def find(number, array):
    low = 0
    high = len(array)-1
    while (low <= high):
        mid = (low+high)//2
        if array[mid][0] > number:
            high = mid-1
        else:
            low = mid+1
    return high


def convert(seed):
    curr = seed
    for map in maps:
        array = maps[map]
        src_idx = find(curr, array)
        if src_idx >= 0 and maps[map][src_idx][1] > curr:
            curr = (curr-maps[map][src_idx][0]) + dst_maps[map][src_idx]
            # print(map, src_idx, maps[map][src_idx], dst_maps[map][src_idx], curr)
    return curr


seeds = ((data[0].strip()).split(": ")[-1]).split()
line_idx = 2
maps = dict()
dst_maps = dict()
map_list = []
while line_idx < len(data):
    line = data[line_idx].strip()
    if line.endswith("map:"):
        map_name = line.split()[0]
        src_map = []
        dst_map = []
        line_idx += 1
        while line_idx < len(data) and (line := data[line_idx].strip()):
            line = line.split()
            src_map.append((int(line[1]), int(line[1])+int(line[2])))
            dst_map.append(int(line[0]))
            line_idx += 1
        maps[map_name] = sorted(src_map[:])
        sorted_dst_idxs = sorted(
            range(len(dst_map)), key=lambda x: src_map[x])
        dst_maps[map_name] = [dst_map[i] for i in sorted_dst_idxs]
        map_list.append(map_name)
    line_idx += 1
# print(maps)


def part1():
    min_convert = 10**9
    for seed in seeds:
        min_convert = min(convert(int(seed)), min_convert)
    return min_convert


def part2():
    min_convert = 10**15
    ranges = []
    for seed_idx in range(0, len(seeds), 2):
        ranges.append((int(seeds[seed_idx]), int(
            seeds[seed_idx])+int(seeds[seed_idx+1])))
    ranges.sort()
    idx = 1
    new_ranges = [ranges[0]]
    for idx in range(1, len(ranges)):
        if ranges[idx][0] <= new_ranges[-1][1]:
            old = new_ranges.pop()
            new_ranges.append((old[0], ranges[idx][1]))
        else:
            new_ranges.append(ranges[idx])
    print(new_ranges, len(new_ranges))
    return min_convert


if __name__ == "__main__":
    print(f"Answer for part one: {part1()}")
    print(f"Answer for part two: {part2()}")
