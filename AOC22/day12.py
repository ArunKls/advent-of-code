from collections import deque

f = open("day12.txt", "r")
data = f.readlines()
f.close()

queue = deque()
vis = set()
sfound, efound = False, False

for i in range(len(data)):
    data[i] = list(data[i].strip())
    for j in range(len(data[0])):
        if data[i][j] == 'S' or data[i][j] == 'a':
            queue.append((i, j))
            vis.add((i, j))
            data[i][j] = 'a'
            # sfound = True
        if data[i][j] == 'E':
            E = (i, j)
            data[i][j] = 'z'
        #     efound = True
        # if sfound and efound:
        #     break


def bfs():
    count = 0
    while queue:
        queuelen = len(queue)
        for elem in range(queuelen):
            pos = queue.popleft()
            if pos == E:
                return count
            for i, j in zip([1, -1, 0, 0], [0, 0, 1, -1]):
                newpos = (pos[0]+i, pos[1]+j)
                if 0 <= newpos[0] < len(data) and 0 <= newpos[1] < len(data[0]):
                    # print("pos", newpos, pos, len(data), len(data[0]))
                    # print(ord(data[newpos[0]][newpos[1]]), ord(data[pos[0]][pos[1]]))
                    if newpos not in vis and ord(data[newpos[0]][newpos[1]]) <= ord(data[pos[0]][pos[1]]) + 1:
                        # print(newpos)
                        queue.append(newpos)
                        vis.add(newpos)
        count += 1
    return -1


print(bfs())
