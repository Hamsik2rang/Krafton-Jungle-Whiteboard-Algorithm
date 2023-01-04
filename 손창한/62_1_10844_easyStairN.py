import sys
input = sys.stdin.readline

def dfs(i, x):
    global cnt
    if not (-1<x<10):
        return
    if i == n:
        cnt += 1
        return
    dfs(i+1, x-1)
    dfs(i+1, x+1)

n = int(input())
cnt = 0
for x in range(1, 10):
    dfs(1, x)
print(cnt)