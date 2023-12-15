

f = open("day15.txt", "r")
data = f.readlines()
f.close()


def hashval(data):
    total = 0
    for bit in data:
        curr = 0
        for char in bit:
            curr += ord(char)
            curr = (curr*17) % 256
        # print(curr)
        total += curr
    return total


def part1():
    global data
    input = data
    input = input[0].strip().split(',')
    return hashval(input)


class Node:
    def __init__(self, label, foc):
        self.label = label
        self.foc = foc
        self.next = None
        self.prev = None

    def __repr__(self) -> str:
        name = f"{self.label} {self.foc}"
        return name


class CLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self) -> str:
        if not self.head:
            return ""
        llist = []
        node = self.head
        while node is not None:
            llist.append(repr(node))
            node = node.next
        return ",".join(llist)

    def push(self, node):
        if not self.tail:
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        node.prev = self.tail
        self.tail = self.tail.next
        return

    def pop(self, node):
        if not node.next or node.prev:
            self.head = None
            self.tail = None
            return
        if node.prev is None:
            node.next.prev = None
            self.head = node.next
            return
        if node.next is None:
            node.prev.next = None
            self.tail = node.prev
            return

        node.next.prev = node.prev
        node.prev.next = node.next
        return


def part2():
    hm = dict()
    global data
    input = data
    input = input[0].strip().split(',')
    total = 0
    for bit in input:
        if bit.endswith('-'):
            label = bit[:-1]
            hash_ = hashval([label])
            if hash_ in hm and label in hm[hash_][1]:
                node = hm[hash_][1][label]
                hm[hash_][0].pop(node)
                hm[hash_][1].pop(label)
        else:
            label, foc = bit.split('=')
            hash_ = hashval([label])
            if hash_ not in hm:
                hm[hash_] = [CLL(), dict()]
            if label in hm[hash_][1]:
                node = hm[hash_][1][label]
                node.foc = foc
            else:
                node = Node(label, foc)
                hm[hash_][1][label] = node
                hm[hash_][0].push(node)
        # print(hm)
    for key in hm.keys():
        ll = hm[key][0]
        i = 1
        node = ll.head
        while node is not None:
            curr = (key+1)*(i)*(int(node.foc))
            i += 1
            node = node.next
            total += curr
    return total


if __name__ == "__main__":
    print(f"Answer for part one: {part1()}")
    print(f"Answer for part two: {part2()}")
