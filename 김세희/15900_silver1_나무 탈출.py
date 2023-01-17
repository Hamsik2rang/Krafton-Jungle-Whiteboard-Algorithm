'''
1. 문제의 시간 제한은?
2초

2. 문제의 최대 N값은?(항상 N이 아닐 수도 있으며, 여러 개일 수도 있음)
500000

3. 1, 2를 바탕으로 이 문제에서 허용하는 최대 시간 복잡도는?
O(N)?

4. 3을 바탕으로 문제를 읽었을 때 사용할 수 있는 알고리즘은?
dfs bfs

5. 왜 4라고 생각했는가?
'''
import sys, sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
cnt = 0
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node, count):
    global cnt
    if visited[node]:
        return

    visited[node] = True
    flag = False
    for next in graph[node]:
        if not visited[next]:
            flag = True
            dfs(next, count+1)
    if not flag:
        cnt+=count
        return

dfs(1,0)

if cnt%2==0:
    print("No")
else:
    print("Yes")