f = open("day10.txt", "r")
data = f.readlines()
f.close()
cycles = [0]
xval = [1]


def find(arr, target):
    l = 0
    r = len(arr)-1
    while l <= r:
        m = (l+r)//2
        if arr[m] >= target:
            r = m-1
        else:
            l = m+1
    return l


for instr in data:
    instr = instr.strip()
    if instr.startswith('addx'):
        instr, add = instr.split()
        cycles.append(cycles[-1]+2)
        xval.append(xval[-1]+int(add))
    else:
        cycles.append(cycles[-1]+1)
        xval.append(xval[-1])
ans = 0
for cycle in [20, 60, 100, 140, 180, 220]:
    idx = find(cycles, cycle)
    ans += cycle*xval[idx-1]
print(ans)

crv = [["." for j in range(40)] for i in range(6)]
cycleidx = 0
for i in range(6):
    for j in range(40):
        cycle = (i*40)+j+1
        if cycle > cycles[cycleidx+1]:
            cycleidx += 1
        sprite = [xval[cycleidx]-1, xval[cycleidx], xval[cycleidx]+1]
        if j in sprite:
            crv[i][j] = "#"
        # print(i, j, cycle, sprite, j in sprite)

for i in range(6):
    print(" ".join(crv[i]))
