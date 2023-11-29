import argparse
import urllib.request as url

argParser = argparse.ArgumentParser()
argParser.add_argument("-n", "--num", help="Day number")

args = argParser.parse_args()

code = f"""

f = open("day{args.num}.txt", "r")
data = f.readlines()
f.close()

def part1():
    pass

def part2():
    pass

if __name__ == "__main__":
    print(f"Answer for part one: {{part1()}}")
    print(f"Answer for part two: {{part2()}}")

"""

f = open(f"day{args.num}.py", "w")
f.write(code)
f.close()


f = open(f"day{args.num}.txt", "w")
f.close
