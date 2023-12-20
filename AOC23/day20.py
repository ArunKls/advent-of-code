from collections import defaultdict, deque
from math import lcm

f = open("day20.txt", "r")
data = f.readlines()
f.close()

flipflop = defaultdict(int)
conjunction = dict()
flow = defaultdict(list)

for line in data:
    inp, dests = line.strip().split(' -> ')
    dests = dests.split(', ')
    if inp.startswith('%'):
        inp = inp[1:]
        flipflop[inp] = 0
    elif inp.startswith('&'):
        inp = inp[1:]
        conjunction[inp] = dict()
    flow[inp] = dests
for line in data:
    inp, dests = line.strip().split(' -> ')
    dests = dests.split(', ')
    if inp != 'broadcaster':
        inp = inp[1:]
    for dest in dests:
        if dest in conjunction:
            conjunction[dest][inp] = 0


def condition():
    for status in flipflop.values():
        if status == 1:
            return False
    for state in conjunction:
        for pls in conjunction[state].values():
            if pls == 1:
                return False
    return True


def part1():
    pulse_count = [0, 0]
    count = 0

    while not count or not condition():
        count += 1
        q = deque()
        pulse_count[0] += 1
        for next in flow['broadcaster']:
            pulse_count[0] += 1
            q.append((next, 0, 'broadcaster'))

        while q:
            # print(q)
            # print("flipflop: ", flipflop, "conjunction: ", conjunction)
            curr, pulse, inp = q.popleft()
            if curr in flipflop:
                if pulse == 0:
                    flipflop[curr] = 1 - flipflop[curr]
                    for next in flow[curr]:
                        pulse_count[flipflop[curr]] += 1
                        q.append((next, flipflop[curr], curr))
            elif curr in conjunction:
                conjunction[curr][inp] = pulse
                send = 0
                for pls in conjunction[curr].values():
                    if pls == 0:
                        send = 1
                        break
                for next in flow[curr]:
                    pulse_count[send] += 1
                    q.append((next, send, curr))
        # print("flipflop: ", flipflop, "conjunction: ", conjunction)
        if count == 1000:
            break
    # print(count, pulse_count)
    return pulse_count[0]*pulse_count[1]


def part2():
    pulse_count = [0, 0]
    count = 0
    freq = defaultdict(list)

    while not count or not condition():
        count += 1
        q = deque()
        pulse_count[0] += 1
        for next in flow['broadcaster']:
            pulse_count[0] += 1
            q.append((next, 0, 'broadcaster'))

        while q:
            # print(q)
            # print("flipflop: ", flipflop, "conjunction: ", conjunction)
            curr, pulse, inp = q.popleft()
            if curr == 'rx' and pulse == 0:
                break
            if curr == 'nr' and pulse == 1:
                freq[inp].append(count)
            if curr in flipflop:
                if pulse == 0:
                    flipflop[curr] = 1 - flipflop[curr]
                    for next in flow[curr]:
                        pulse_count[flipflop[curr]] += 1
                        q.append((next, flipflop[curr], curr))
            elif curr in conjunction:
                conjunction[curr][inp] = pulse
                send = 0
                for pls in conjunction[curr].values():
                    if pls == 0:
                        send = 1
                        break
                for next in flow[curr]:
                    pulse_count[send] += 1
                    q.append((next, send, curr))
        # print("flipflop: ", flipflop, "conjunction: ", conjunction)
        if len(freq.keys()) > 0 and all([len(freq[inp]) >= 2 for inp in freq]):
            diffs = [freq[inp][1]-freq[inp][0] for inp in freq]
            return lcm(*diffs)
    # print(count, pulse_count, pulse_count[0]*pulse_count[1])


if __name__ == "__main__":
    print(f"Answer for part one: {part1()}")
    print(f"Answer for part two: {part2()}")
