f = open("day6.txt", "r")
data = f.read()
f.close()
window = list(data[:14])
for i in range(14, len(data)):
    if len(set(window)) < 14:
        window.pop(0)
        window.append(data[i])
    else:
        print(i)
        break