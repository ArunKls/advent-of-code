f = open("day4.txt", "r")
data = f.readlines()
f.close()
count = 0
# for pair in data:
#     ranges = pair.strip().split(",")
#     range1, range2 = ranges[0].split("-"), ranges[1].split("-")
#     if int(range1[0]) > int(range2[0]):
#         range1, range2 = range2[:], range1[:]
#     elif int(range1[0]) == int(range2[0]):
#         count += 1
#         continue
#     if int(range2[1]) <= int(range1[1]):
#         count += 1
# print(count)
for pair in data:
    ranges = pair.strip().split(",")
    range1, range2 = ranges[0].split("-"), ranges[1].split("-")
    if int(range1[0]) > int(range2[0]):
        range1, range2 = range2[:], range1[:]
    elif int(range1[0]) == int(range2[0]):
        count += 1
        continue
    if int(range2[0]) <= int(range1[1]):
        count += 1
print(count)
