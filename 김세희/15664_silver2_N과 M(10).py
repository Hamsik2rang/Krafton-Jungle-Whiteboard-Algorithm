'''
1. 문제의 시간 제한은?
1초

2. 문제의 최대 N값은?(항상 N이 아닐 수도 있으며, 여러 개일 수도 있음)
8

3. 1, 2를 바탕으로 이 문제에서 허용하는 최대 시간 복잡도는?
뭐든????

4. 3을 바탕으로 문제를 읽었을 때 사용할 수 있는 알고리즘은?
dfs

5. 왜 4라고 생각했는가?
dfs으로 풀어도 넉넉할 것 같음

처음에 자연수를 받고, 오름차순 정렬을 한 뒤, 첫 번째 수부터 시작해서 수를
모으거나 모으지 않는 dfs를 돌린다.
만약 토탈 수가 m과 같아지면 print 시킨다.
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numList = list(map(int, input().split()))
visited = []

numList.sort()

def dfs(idx, now, cnt):
    if cnt==m:
        if now in visited:
            return
        print(" ".join(map(str, now)))
        visited.append(now)
        return
    if idx==n:
        return
    
    dfs(idx+1, now + [numList[idx]], cnt+1)
    dfs(idx+1, now, cnt)

dfs(0, [], 0)