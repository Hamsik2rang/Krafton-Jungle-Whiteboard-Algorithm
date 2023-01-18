'''
1. 문제의 시간 제한은?
1초

2. 문제의 최대 N값은?(항상 N이 아닐 수도 있으며, 여러 개일 수도 있음)
100
m <= 100000

3. 1, 2를 바탕으로 이 문제에서 허용하는 최대 시간 복잡도는?
n^4

4. 3을 바탕으로 문제를 읽었을 때 사용할 수 있는 알고리즘은?
플로이드 워셜

5. 왜 4라고 생각했는가?
모든 정점에서 다른 모든 정점까지의 최솟값을 구해야 해서
'''
import sys
inf = sys.maxsize
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[inf]*(n+1) for _ in range(n+1)]

for i in range(n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b],c)

for k in range(1, n+1):
    for start in range(1, n+1):
        for end in range(1, n+1):
            graph[start][end] = min(graph[start][end], graph[start][k] + graph[k][end])

for i in range(1, n+1):
    print(' '.join(map(lambda x: '0' if x==inf else str(x), graph[i][1:])))
