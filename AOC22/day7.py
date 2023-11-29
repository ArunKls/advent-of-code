f = open("day7.txt", "r")
data = f.readlines()
f.close()


class Node:
    def __init__(self, name, size=0, dir=True, parent=None):
        self.name = name
        if dir:
            self.children = dict()
        else:
            self.children = False
        self.size = size
        self.parent = parent


root = Node("/")
curr_node = root
l = 1
while l < len(data):
    line = data[l].strip()
    # print(line)
    if line.startswith("$ cd .."):
        curr_node = curr_node.parent
    elif line.startswith("$ cd"):
        curr_node = curr_node.children[line.split()[-1]]
    elif line.startswith("$ ls"):
        l += 1
        while l < len(data) and not data[l].startswith("$"):
            f = data[l].split()
            if f[0] == "dir":
                curr_node.children[f[1]] = Node(f[1], parent=curr_node)
            else:
                curr_node.children[f[1]] = Node(
                    f[1], size=int(f[0]), dir=False, parent=curr_node)
            l += 1
        l -= 1
    l += 1

ans = []


def dfs(node):
    if not node:
        # print("1", node.name)
        return
    if not node.children:
        # print("2", node.name)
        return node.size
    size = 0
    for name, child in node.children.items():
        # print("3", name)
        size += dfs(child)
    node.size = size
    if node.children:
        # print(node.size)
        ans.append(node.size)
    return size


root_size = dfs(root)
unused = 70000000 - root_size
delete = 30000000 - unused
ans.sort()
## Lower Bound Code
low = 0
high = len(ans)-1
ret = len(ans)
while (low <= high):
    mid = (low+high)//2
    if ans[mid] >= delete:
        high = mid-1
    else:
        low = mid+1
print(ans)
print(ans[low])
