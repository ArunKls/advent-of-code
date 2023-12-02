

f = open("day2.txt", "r")
data = f.readlines()
f.close()

def part1():
    counter = 0
    ans = 0
    color_dict = {"red": 12, "green": 13, "blue": 14}
    for line in data:
        counter += 1
        line = line.strip()
        records = (line.split(": ")[-1]).split("; ")
        flag = True
        for record in records:
            if flag:
                cubes = record.split(", ")
                for cube in cubes:
                    number, color = cube.split()
                    if int(number) > color_dict[color]:
                        flag = False
        if flag:
            ans += counter
    return ans


def part2():
    ans = 0
    for line in data:
        line = line.strip()
        records = (line.split(": ")[-1]).split("; ")
        cube_dict = {"red": 0, "green": 0, "blue": 0}
        for record in records:
            cubes = record.split(", ")
            for cube in cubes:
                number, color = cube.split()
                cube_dict[color] = max(cube_dict[color], int(number))
        power = cube_dict["red"]*cube_dict["green"]*cube_dict["blue"]
        ans += power
    return ans

if __name__ == "__main__":
    print(f"Answer for part one: {part1()}")
    print(f"Answer for part two: {part2()}")

