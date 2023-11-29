f = open("day3.txt", "r")
data = f.readlines()
f.close()
score = 0
# for sack in data:
#     sack = list(sack.strip())
#     comp1 = set(sack[:len(sack)//2])
#     comp2 = set(sack[len(sack)//2:])
#     rep = comp1.intersection(comp2)
#     val = ord(rep.pop())
#     if 65 <= val <= 90:
#         score += val-38
#     else:
#         score += val-96
# print(score)

for i in range(0, len(data), 3):
    sack1 = set(list(data[i].strip()))
    sack2 = set(list(data[i+1].strip()))
    sack3 = set(list(data[i+2].strip()))
    rep = sack1.intersection(sack2)
    rep = rep.intersection(sack3)
    val = ord(rep.pop())
    if 65 <= val <= 90:
        score += val-38
    else:
        score += val-96
print(score)
