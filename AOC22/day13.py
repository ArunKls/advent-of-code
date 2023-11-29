from collections import deque

f = open("day13.txt", "r")
data = f.readlines()
f.close()


def process(arr):
    return eval(arr)


def compare(left, right):
    l = min(len(left), len(right))
    for i in range(l):
        if type(left[i]) is list and type(right[i]) is list:
            # print(1)
            return compare(left[i], right[i])
        elif type(left[i]) is int and type(right[i]) is int:
            # print(2)
            if left[i] > right[i]:
                return False
        else:
            if type(left[i]) is list:
                # print(3)
                return compare(left[i], [right[i]])
            else:
                # print(4)
                return compare([left[i]], right[i])
    if len(left) > len(right):
        return False
    return True


ans = 0
val = 1
for i in range(0, len(data), 3):
    left = data[i].strip()
    right = data[i+1].strip()

    left = process(left)
    right = process(right)

    if compare(left, right):
        print(left)
        print(right, True)
        ans += val
    else:
        print(left)
        print(right, False)
    val += 1
print(ans)
