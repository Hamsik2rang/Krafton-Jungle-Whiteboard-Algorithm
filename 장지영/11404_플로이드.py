'''
플로이드-워셜 최단경로 알고리즘 문제
모든 정점에서 모든 정점까지 가는 최단경로 구하는 알고리즘
다익스트라와 비슷하지만 DP를 이용해 매번 최단노드를 계산할 필요는 없다
시간복잡도 : O(N^3)
노드 간선의 개수가 모두 많으면 우선순위큐 다익스트라를 이용하는게 편하다고 한다. O(ElogV)
    
    ## 플로이드 - 워셜 알고리즘 ###
    시간복잡도 O(N^3)
    
    1. 노드의 간선을 확인하고 최단 거리 비용 테이블을 생성한다. 2차원 배열로 관리 
        갈 수 없는 곳은 무한, 자기 자신으로 가는 비용은 0
    2. 1번 노드를 거쳐 가는 경우를 고려하여 최단 거리를 갱신. 
        - 현재 확인하고 있는 노드를 제외하고, n-1 개의 노드 중 서로 다른 노드 쌍(A, B)를 선택한다.
        - (A->B)비용 > (A->1번 노드->B)비용 이라면 최단거리 갱신. 
    3. 나머지 노드에 대해서도 마찬가지로 돌린다.    
'''
import sys
input = sys.stdin.readline

cityN = int(input())
busM = int(input())
INFIN = 1_0000_0000


# 도시 번호는 1부터 N 까지 
floyd = [[INFIN for _ in range(cityN + 1)]for __ in range(cityN + 1)]


# initialize graph : path to self = 0
for i in range(1, cityN + 1) : 
    floyd[i][i] = 0


# insert edges(bus road)
for bus in range(busM) : 
    start, end, money = list(map(int, input().split()))
    if floyd[start][end] > money : 
        floyd[start][end] = money

# floyd-warshal algorithm O(V^3)
for testC in range(1, cityN + 1) : # test for passing through every city 
    for start in range(1, cityN + 1) : 
        for dest in range(1, cityN + 1) :
            if floyd[start][dest] > (floyd[start][testC] + floyd[testC][dest]) : 
                # min cost update 
                floyd[start][dest] = floyd[start][testC] + floyd[testC][dest]

# print result 
for i in range(1, cityN + 1) : 
    for j in range(1, cityN + 1) : 
        if floyd[i][j] == INFIN : 
            print(0, end = ' ')
        else : 
            print(floyd[i][j], end = ' ')
    print()