f = open("day8.txt", "r")
data = f.readlines()
f.close()
visible = set()

m = len(data)
n = len(data[0].strip())

products = [[1 for i in range(n)] for j in range(m)]


def mstack(arr, row=True):
    # curr = arr[0]
    # for i in range(1, len(arr)):
    #     if arr[i][0] > curr[0]:
    #         visible.add(curr[1])
    #         curr = arr[i]
    # visible.add(curr[1])
    stack = []
    for i in range(len(arr)):
        while stack and arr[stack[-1][0]][0] <= arr[i][0]:
            curr = stack.pop()
            if row:
                products[curr[1][0]][curr[1][1]] *= abs(i-curr[1][1])
            else:
                products[curr[1][0]][curr[1][1]] *= abs(i-curr[1][0])
        stack.append((i, arr[i][1]))
    nextHigh = len(arr)-1
    while stack:
        curr = stack.pop()
        if row:
            products[curr[1][0]][curr[1][1]] *= abs(nextHigh-curr[1][1])
        else:
            products[curr[1][0]][curr[1][1]] *= abs(nextHigh-curr[1][0])
        # nextHigh = curr[0]
    # print(products)
    for i in range(len(arr)-1, -1, -1):
        while stack and arr[stack[-1][0]][0] <= arr[i][0]:
            curr = stack.pop()
            if row:
                products[curr[1][0]][curr[1][1]] *= abs(i-curr[1][1])
            else:
                products[curr[1][0]][curr[1][1]] *= abs(i-curr[1][0])
        stack.append((i, arr[i][1]))
    nextHigh = 0
    while stack:
        curr = stack.pop()
        if row:
            products[curr[1][0]][curr[1][1]] *= abs(nextHigh-curr[1][1])
        else:
            products[curr[1][0]][curr[1][1]] *= abs(nextHigh-curr[1][0])
        # nextHigh = curr[0]


# print(m, n)
for i in range(m):
    row = []
    for j in range(n):
        # print(data[i], j, data[i][j])
        row.append((data[i][j], (i, j)))
    mstack(row)
    # row.reverse()
    # mstack(row)
for j in range(n):
    col = []
    for i in range(m):
        col.append((data[i][j], (i, j)))
    mstack(col, False)
    # col.reverse()
    # mstack(col, False)
# print(visible)
maxscore = 0
for i in range(1, m-1):
    for j in range(1, n-1):
        maxscore = max(maxscore, products[i][j])
print(maxscore)
print(products)
