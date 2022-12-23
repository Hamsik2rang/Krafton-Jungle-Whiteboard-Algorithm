"""
[백준]5014-스타트링크
스타트링크는 총 F층으로 이루어진 고층 건물에 사무실이 있고, 
스타트링크가 있는 곳의 위치는 G층이다. 
강호가 지금 있는 곳은 S층이고, 이제 엘리베이터를 타고 G층으로 이동하려고 한다.
보통 엘리베이터에는 어떤 층으로 이동할 수 있는 버튼이 있지만, 
강호가 탄 엘리베이터는 버튼이 2개밖에 없다. U버튼은 위로 U층을 가는 버튼, D버튼은 아래로 D층을 가는 버튼이다. 
(만약, U층 위, 또는 D층 아래에 해당하는 층이 없을 때는, 엘리베이터는 움직이지 않는다)

[입력]
첫째 줄에 F, S, G, U, D가 주어진다. 
(1 ≤ S, G ≤ F ≤ 1000000, 0 ≤ U, D ≤ 1000000) 건물은 1층부터 시작하고, 가장 높은 층은 F층이다.

"""
import sys
sys.stdin=open("./input.txt", 'r')

import sys
from collections import deque
sys.setrecursionlimit(10**4)
input=sys.stdin.readline

f,s,g,u,d=map(int,input().split())
visit=[0 for _ in range(f+1)]
count=[0 for _ in range(f+1)]

def bfs(v):
    q=deque([v])
    visit[v]=1
    print(q)
    while q:
        v=q.popleft()
        if v==g:
            return print(count[g])
        for i in (v+u, v-d):
            if 0<i<=f and not visit[i]:
                visit[i]=1
                count[i]=count[v]+1
                q.append(i)
        print(q)
        print(count)
        
    if count[g]==0:
        return print("use the stairs")
    
bfs(s)