import sys

sys.setrecursionlimit(10**5 * 2)


class Node:
    def __init__(self, num):
        self.num = num
        self.height = 0
        self.parent = None
        self.child = []


node_pool = [Node(i) for i in range(50001)]


def set_tree(x: int) -> None:
    global check
    check[x] = True
    for next in graph[x]:
        if check[next]:
            continue
        node_pool[next].parent = x
        node_pool[next].height = node_pool[x].height + 1
        set_tree(next)


n = int(sys.stdin.readline())
graph = [[] for _ in range(n + 1)]
check = [False for _ in range(n + 1)]
for i in range(n - 1):
    src, dest = map(int, sys.stdin.readline().split())
    graph[src].append(dest)
    graph[dest].append(src)

set_tree(1)

m = int(sys.stdin.readline())
for i in range(m):
    left, right = map(int, sys.stdin.readline().split())

    while node_pool[left].height > node_pool[right].height:
        left = node_pool[left].parent
    while node_pool[left].height < node_pool[right].height:
        right = node_pool[right].parent

    while node_pool[left].num != node_pool[right].num:
        left = node_pool[left].parent
        right = node_pool[right].parent
    print(node_pool[left].num)
