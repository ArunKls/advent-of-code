

f = open("day24.txt", "r")
data = f.readlines()
f.close()


def intersect(pos1, vel1, pos2, vel2):
    slope1 = vel1[1]/vel1[0] if vel1[0] != 0 else 100000
    slope2 = vel2[1]/vel2[0] if vel2[0] != 0 else 100000
    if slope1 == slope2:
        return None, None
    x = (pos2[1] - pos1[1] + slope1*pos1[0] -
         slope2*pos2[0])/(slope1-slope2)
    if ((vel1[0] > 0) ^ (x > pos1[0])) or ((vel2[0] > 0) ^ (x > pos2[0])):
        return None, None
    y = slope1*(x - pos1[0]) + pos1[1]
    # print(pos1, pos2, x, y)
    if ((vel1[1] > 0) ^ (y > pos1[1])) or ((vel2[1] > 0) ^ (y > pos2[1])):
        return None, None
    return x, y

stones = []
for line in data:
    line = line.strip()
    pos, vel = line.split(' @ ')
    pos = pos.split(', ')
    pos = [int(pos[0]), int(pos[1]), int(pos[2])]
    vel = vel.split(', ')
    vel = [int(vel[0]), int(vel[1]), int(vel[2])]
    stones.append([pos, vel])

def part1():
    count = 0
    for i in range(len(stones)):
        for j in range(i+1, len(stones)):
            pos1, vel1 = stones[i]
            pos2, vel2 = stones[j]
            x, y = intersect(pos1, vel1, pos2, vel2)
            if x and y and 200000000000000 < x <= 400000000000000 and 200000000000000 < y <= 400000000000000:
                count += 1
    return count

def part2():
    intersecting = False
    n = 1
    while not intersecting:
        point = None
        for vx in range(n):
            vy = n - vx
            for dvx, dvy in zip([-1*vx, vx], [-1*vy, vy]):
                # print(dvx, dvy)
                i = 0
                while i < len(stones):
                    point = None
                    for j in range(len(stones)):
                        if i==j:
                            continue
                        pos1, vel1 = stones[i]
                        pos2, vel2 = stones[j]
                        vel1 = [vel1[0]+dvx, vel1[1]+dvy, vel1[2]]
                        vel2 = [vel2[0]+dvx, vel2[1]+dvy, vel2[2]]
                        x, y = intersect(pos1, vel1, pos2, vel2)
                        if not x or not y:
                            point = None
                            break
                        if not point:
                            point = (x, y)
                        elif point != (x, y):
                            break
                    if point:
                        break
                    i += 1
            if point:
                break
        n += 1
    return point
        



if __name__ == "__main__":
    print(f"Answer for part one: {part1()}")
    print(f"Answer for part two: {part2()}")
