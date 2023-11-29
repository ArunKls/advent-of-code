stacks = [["B", "W", "N"], ["L", "Z", "S", "P", "T", "D", "M", "B"], ["Q", "H", "Z", "W", "R"],
          ["W", "D", "V", "J", "Z", "R"], ["S", "H", "M", "B"],
          ["L", "G", "N", "J", "H", "V", "P", "B"], [
              "J", "Q", "Z", "F", "H", "D", "L", "S"],
          ["W", "S", "F", "J", "G", "Q", "B"], ["Z", "W", "M", "S", "C", "D", "J"]]

f = open("day5.txt", "r")
data = f.readlines()
f.close()

for instr in data:
    instr = instr.strip().split()
    moves, fr, to = int(instr[1]), int(instr[3])-1, int(instr[5])-1
    pick = stacks[fr][-moves:]
    # print("Before:", stacks[fr], stacks[to], moves)
    stacks[fr] = stacks[fr][:-moves]
    stacks[to].extend(pick)
    # print("After:", stacks[fr], stacks[to])
ans = ""
for stack in stacks:
    ans += stack[-1]
print(ans)
