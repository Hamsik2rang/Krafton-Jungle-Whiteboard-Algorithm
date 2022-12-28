'''
1. 문제의 시간 제한은?
2초

2. 문제의 최대 N값은?(항상 N이 아닐 수도 있으며, 여러 개일 수도 있음)
500

3. 1, 2를 바탕으로 이 문제에서 허용하는 최대 시간 복잡도는?
ON^3?

4. 3을 바탕으로 문제를 읽었을 때 사용할 수 있는 알고리즘은?
DFS

5. 왜 4라고 생각했는가?
널널해서 그냥 완전탐색을 해도 되겠다. 라고 생각했다.
'''


import sys
input = sys.stdin.readline

t = int(input())

def dfs(chapList, idx, total, len):
    global minVal, k
    if visited[idx]: return
    visited[idx] = True
    if len == k:
        minVal = min(total + chapList[idx], minVal)
        return

    for i in range(k):
        if not visited[i]:
            dfs(chapList, i, total + chapList[idx], len+1)
            visited[i] = False

for _ in range(t):
    k = int(input())
    chapters = list(map(int, input().split()))
    visited = [False] * k
    minVal = sys.maxsize
    for i in range(k):
        dfs(chapters, i, chapters[i], 1)
    print(minVal)