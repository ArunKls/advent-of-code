

f = open("day19.txt", "r")
data = f.readlines()
f.close()

workflows = dict()
flows = True
parts = []
for line in data:
    line = line.strip()
    if not line:
        flows = False
        continue
    if flows:
        name, val = line.split('{')
        val = val[:-1].split(',')
        workflows[name] = val
    else:
        part = dict()
        vals = line[1:-1].split(',')
        for val in vals:
            val = val.split('=')
            part[val[0]] = int(val[1])
        parts.append(part)


def part1():
    total = 0
    for part in parts:
        x, m, a, s = part['x'], part['m'], part['a'], part['s']
        curr = 'in'
        while True:
            if curr == 'R':
                break
            elif curr == 'A':
                total += x + m + a + s
                break
            rules = workflows[curr]
            for rule in rules[:-1]:
                rule, dest = rule.split(':')
                if eval(rule):
                    curr = dest
                    break
            else:
                curr = rules[-1]
    return total

# From leijurv's solution
def part2():
    ranges = {'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]}

    def both(ch, gt, val, ranges):
        ch = 'xmas'.index(ch)
        ranges2 = []
        for rng in ranges:
            rng = list(rng)
            lo, hi = rng[ch]
            if gt:
                lo = max(lo, val + 1)
            else:
                hi = min(hi, val - 1)
            if lo > hi:
                continue
            rng[ch] = (lo, hi)
            ranges2.append(tuple(rng))
        return ranges2

    def calc(w):
        it = w[0]
        if it == "R":
            return []
        if it == "A":
            return [((1, 4000), (1, 4000), (1, 4000), (1, 4000))]
        if ":" not in it:
            return calc(workflows[it])
        cond = it.split(":")[0]
        gt = ">" in cond
        ch = cond[0]
        val = int(cond[2:])
        val_inverted = val + 1 if gt else val - 1
        if_cond_is_true = both(
            ch, gt, val, calc([it.split(":")[1]]))
        if_cond_is_false = both(ch, not gt, val_inverted,
                                calc(w[1:]))
        return if_cond_is_true + if_cond_is_false
    ans = 0
    for rng in calc(workflows['in']):
        v = 1
        for lo, hi in rng:
            v *= hi - lo + 1
        ans += v
    return ans


if __name__ == "__main__":
    print(f"Answer for part one: {part1()}")
    print(f"Answer for part two: {part2()}")
