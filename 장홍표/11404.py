'''
100개의 노드, 100,000개의 간선으로 이루어진 최소비용
    -> BFS (비용으로 계산하여 q삽입할것!)
    -> DP도 사용! (안쓰면 너무 오래걸리고, 반복작업이 생김)
    -> cklist사용하여 반복안되게!(DP를 visited로 활용)
<<input>>
1C : 도시의 수
2C : 버스의 수
3C : 출발도시, 도착도시, 비용
<<output>>
1C: 1번도시에서 각 도시까지 가는 버스비용 (1번비용(0) 2번비용...)
2C: 2번도시에서...
<<hint>>
플로이드 워셜?
'''
import sys
input = sys.stdin.readline
from collections import deque
inf = 10_000_001
N = int(input())
M = int(input())
Citys = [[ inf for _ in range(N+1)] for _ in range(N+1)]
q = deque()
for i in range(N+1):
    Citys[i][i] = 0
"""사용할 변수 초기화"""

for _ in range(M):
    start, end, cost = map(int, input().strip().split())
    Citys[start][end] = min(Citys[start][end], cost)
"""input값 입력"""

for i in range(1,N+1):
    for j in range(1,N+1):
        if(i!=0 and j!=0 and Citys[i][j]!=0 and Citys[i][j]!=inf):
            q.append((i, j, Citys[i][j]))
    while(q):
        start, now, cost = q.popleft()
        for k in range(1,N+1):
            if(k!=start and k!=now and (Citys[start][k] > Citys[now][k] + cost)):
                Citys[start][k] = Citys[now][k] + cost
                if(now>i):
                    q.append((start, k , Citys[now][k] + cost))


    
#q에 넣을 항목...? 출발도시 / 현재도시 / 현재코스트! 출->현재도시 min비교 기록

#test 출력
# print(Citys[1][2])
for i in range(1, N+1):
    for j in range(1, N+1):
        if (Citys[i][j] == inf):
            Citys[i][j] = 0
        print(Citys[i][j], end=' ')
    print()