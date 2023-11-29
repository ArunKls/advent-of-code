f = open("day9.txt", "r")
data = f.readlines()
f.close()
head = (4, 0)
tail = (4, 0)
visited = {(4, 0)}
moveDict = {'L': [0, -1], 'R': [0, 1], 'D': [1, 0], 'U': [-1, 0]}


def non_diag(head, tail):
    return abs(head[0]-tail[0]) == 0 or abs(head[1]-tail[1]) == 0

def overlap(head, tail):
    return abs(head[0]-tail[0]) == 0 and abs(head[1]-tail[1]) == 0

def adjacent(head, tail):
    return (abs(head[0]-tail[0]) == 1 or abs(head[1]-tail[1]) == 1 or overlap) and (abs(head[0]-tail[0]) <= 1 and abs(head[1]-tail[1]) <= 1)

def makeMove(head, tail):
    head = positions[head]
    tail = positions[tail]
    if adjacent(head, tail):
        pass
    elif non_diag(head, tail):
        # print("tail move", tail)
        if head[0] == tail[0]:
            if head[1] > tail[1]:
                tail = (tail[0], tail[1]+1)
            else:
                tail = (tail[0], tail[1]-1)
        else:
            if head[0] > tail[0]:
                tail = (tail[0]+1, tail[1])
            else:
                tail = (tail[0]-1, tail[1])
        # print("tail moved", tail)
    else:
        # print("tail move", tail)
        if head[0] > tail[0]:
            if head[1] > tail[1]:
                tail = (tail[0]+1, tail[1]+1)
            else:
                tail = (tail[0]+1, tail[1]-1)
        else:
            if head[1] > tail[1]:
                tail = (tail[0]-1, tail[1]+1)
            else:
                tail = (tail[0]-1, tail[1]-1)
        # print("tail moved", tail)
    return tail

# for move in data:
#     move = move.strip()
#     dir, steps = move.split()
#     for step in range(int(steps)):
#         # print("head move", head)
#         head = (head[0]+moveDict[dir][0], head[1]+moveDict[dir][1])
#         # print("head moved", head)
#         if adjacent(head, tail):
#             pass
#         elif non_diag(head, tail):
#             # print("tail move", tail)
#             if head[0] == tail[0]:
#                 if head[1] > tail[1]:
#                     tail = (tail[0], tail[1]+1)
#                 else:
#                     tail = (tail[0], tail[1]-1)
#             else:
#                 if head[0] > tail[0]:
#                     tail = (tail[0]+1, tail[1])
#                 else:
#                     tail = (tail[0]-1, tail[1])
#             # print("tail moved", tail)
#         else:
#             # print("tail move", tail)
#             if head[0] > tail[0]:
#                 if head[1] > tail[1]:
#                     tail = (tail[0]+1, tail[1]+1)
#                 else:
#                     tail = (tail[0]+1, tail[1]-1)
#             else:
#                 if head[1] > tail[1]:
#                     tail = (tail[0]-1, tail[1]+1)
#                 else:
#                     tail = (tail[0]-1, tail[1]-1)
#             # print("tail moved", tail)
#         visited.add(tail)
#         # print(head, tail)
# print(len(visited))
positions = {i: (0, 0) for i in range(10)}
visited = {(0, 0)}
for move in data:
    move = move.strip()
    dir, steps = move.split()
    for step in range(int(steps)):
        positions[0] = (positions[0][0]+moveDict[dir][0], positions[0][1]+moveDict[dir][1])
        curr = 0
        for i in range(1, 10):
            positions[i] = makeMove(curr, i)
            curr = i
        visited.add(positions[9])
        # print(dir, positions[9], positions)
print(len(visited))