f = open("day1.txt", "r")
data = f.readlines()
f.close()
total = 0
# maxTotal = 0
# for line in data:
#     if line != '\n':
#         total += int(line)
#     else:
#         maxTotal = max(total, maxTotal)
#         total = 0
# print(maxTotal)
vals = []
for line in data:
    if line != '\n':
        total += int(line)
    else:
        vals.append(total)
        total = 0
vals.sort(reverse=True)
print(vals)
print(sum(vals[:3]))
