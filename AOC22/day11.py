from collections import defaultdict
f = open("day11.txt", "r")
data = f.readlines()
f.close()

items = []
formula = []
test = []

idx = 0
num = 0
for idx_iter in range(0, len(data), 7):
    idx = idx_iter
    line = data[idx].strip()
    if not line.startswith("Monkey"):
        continue
    num = int(line.split()[-1][0])
    idx += 1
    line = data[idx].strip()
    monkey_items = []
    item_list = line.split(': ')[-1]
    for i in item_list.split(', '):
        monkey_items.append(int(i))
    items.append(monkey_items)
    idx += 1
    line = data[idx].strip()
    formula.append(line.split(': ')[-1])
    monkey_test = []
    for i in range(3):
        idx += 1
        line = data[idx].strip()
        monkey_test.append(int(line.split()[-1]))
    test.append(monkey_test)

counts = [0 for i in range(num+1)]

for round in range(1000):
    for monkey in range(num+1):
        # print(items)
        items_list = items[monkey]
        # print(items_list)
        counts[monkey] += len(items_list)
        while items_list:
            item = items_list.pop(0)
            new = 0
            old = item
            exec(formula[monkey])
            new = new // 3
            # print(monkey, test[monkey])
            if new % test[monkey][0] == 0:
                items[test[monkey][1]].append(new)
            else:
                items[test[monkey][2]].append(new)
# print(items)
counts.sort(reverse=True)
print(counts[0]*counts[1])
