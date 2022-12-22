import sys

sys.stdin = open("input.txt", "r")

import sys

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# def union_parent(parent, a, b):
#     parent1 = find_parent(parent, a)
#     parent2 = find_parent(parent, b)
#     if a == b:
#         return
#     parent[parent1] = parent2

isles = int(sys.stdin.readline())
parent = [i for i in range(isles + 1)]
ans = []

print(parent)
for _ in range(isles - 2):
    a, b = map(int, sys.stdin.readline().split())
    parent1 = find_parent(parent, a)
    parent2 = find_parent(parent, b)
    if parent1 == parent2:
       continue
    parent[parent1] = parent2

print(parent)

for i in range(1, isles + 1):
    if i == parent[i]:
        ans.append(i)

print(ans)


