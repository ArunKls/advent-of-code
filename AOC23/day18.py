

f = open("day18.txt", "r")
data = f.readlines()
f.close()

def area(pos, perimeter):
    total = 0
    for i in range(len(pos)):
        next = (i+1) % len(pos)
        prev = (i-1) % len(pos)
        total += pos[i][0]*(pos[prev][1]-pos[next][1])
    return total//2 + 1 + perimeter//2

def part1():
    pos = [[0, 0]]
    row, col = 0, 0
    perimeter = 0
    for line in data:
        line = line.strip().split()
        if line[0] == 'R':
            col += int(line[1])
        elif line[0] == 'L':
            col -= int(line[1])
        elif line[0] == 'U':
            row -= int(line[1])
        else:
            row += int(line[1])
        perimeter += int(line[1])
        pos.append([row, col])
    pos.pop()
    # print(perimeter)
    return area(pos, perimeter)


def part2():
    pos = [[0, 0]]
    row, col = 0, 0
    perimeter = 0
    for line in data:
        line = line.strip().split()
        move = int(line[2][2:-2], 16)
        if line[2][-2] == '0':
            col += move
        elif line[2][-2] == '2':
            col -= move
        elif line[2][-2] == '3':
            row -= move
        else:
            row += move
        perimeter += move
        pos.append([row, col])
    pos.pop()
    # print(perimeter)
    return area(pos, perimeter)


if __name__ == "__main__":
    print(f"Answer for part one: {part1()}")
    print(f"Answer for part two: {part2()}")
