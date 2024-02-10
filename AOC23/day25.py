import networkx as nx
from collections import defaultdict

f = open("day25.txt", "r")
data = f.readlines()
f.close()

G = nx.Graph()


def part1():
    E = defaultdict(set)
    for line in data:
        line = line.strip()
        k, v = line.split(": ")
        v = v.split(" ")
        for vi in v:
            E[k].add(vi)
            E[vi].add(k)
    n = len(E)
    G = nx.DiGraph()
    for k, vs in E.items():
        for v in vs:
            G.add_edge(k, v, capacity=1.0)
            G.add_edge(v, k, capacity=1.0)

    for x in [list(E.keys())[0]]:
        for y in E.keys():
            if x != y:
                cut_value, (L, R) = nx.minimum_cut(G, x, y)
                if cut_value == 3:
                    return (len(L)*len(R))


def part2():
    return "Push the button!"


if __name__ == "__main__":
    print(f"Answer for part one: {part1()}")
    print(f"Answer for part two: {part2()}")
