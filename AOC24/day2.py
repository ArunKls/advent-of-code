

f = open("day2.txt", "r")
data = f.readlines()
f.close()

def part1():
    ans = 0
    for line in data:
        nums = line.split()
        inc = False
        if int(nums[1]) > int(nums[0]):
            inc = True
        flag = True
        for idx in range(1, len(nums)):
            if not flag:
                break
            if inc:
                if not (int(nums[idx]) > int(nums[idx-1]) and 1 <= int(nums[idx]) - int(nums[idx-1]) <= 3):
                    flag = False
            else:
                if not (int(nums[idx]) < int(nums[idx-1]) and 1 <= int(nums[idx-1]) - int(nums[idx]) <= 3):
                    flag = False
        if flag:
            ans += 1
    return ans

def check(line):
    if type(line) == str:
        nums = line.split()
    else:
        nums = line
    inc = False
    if int(nums[1]) > int(nums[0]):
        inc = True
    flag = True
    for idx in range(1, len(nums)):
        if not flag:
            break
        if inc:
            if not (int(nums[idx]) > int(nums[idx-1]) and 1 <= int(nums[idx]) - int(nums[idx-1]) <= 3):
                flag = False
        else:
            if not (int(nums[idx]) < int(nums[idx-1]) and 1 <= int(nums[idx-1]) - int(nums[idx]) <= 3):
                flag = False
    return flag


def part2():
    ans = 0
    for line in data:
        
        if check(line):
            ans += 1
        else:
            line = line.split(" ")
            for i in range(len(line)):
                if check(line[:i] + line[i+1:]):
                    ans += 1
                    break
    return ans

if __name__ == "__main__":
    print(f"Answer for part one: {part1()}")
    print(f"Answer for part two: {part2()}")

