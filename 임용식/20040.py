import sys

sys.setrecursionlimit(10**6)
# sys.stdin = open("input.txt", "r")


def find_set(v: int) -> int:
    global parent
    if parent[v] == v:
        return v
    parent[v] = find_set(parent[v])
    return parent[v]


def union_set(u: int, v: int) -> None:
    global parent
    parent[find_set(v)] = find_set(u)


n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n)]
answer = 0
for i in range(1, m + 1):
    a, b = map(int, sys.stdin.readline().split())
    if find_set(a) == find_set(b) and not answer:
        answer = i
    union_set(a, b)
print(answer)
