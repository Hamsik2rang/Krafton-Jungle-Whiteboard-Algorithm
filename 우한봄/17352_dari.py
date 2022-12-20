import sys
sys.stdin=open("input.txt","r")
input=sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        a, b = b, a
    parent[b] = a

n=int(input())
parent = {i: i for i in range(1, n+1)}
for _ in range(n-2):
    a, b = map(int, input().split())
    union(a, b)
    
pivot = find(1)
for i in range(2, n+1):
    if pivot != find(i):
        print(pivot, i)
        exit()