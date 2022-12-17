"""
문제: 재귀로 부모노드를 하나하나 타고 올라가 공통 부모를 찾으면, 시간초과 => 25000x25000xm(10000)=6조?
1. 각 노드가 depth 별 Parent table을 갖도록 한다. ok
2. 두 노드가 주어졌을 때, 더 깊은 depth를 가진 노드의 depth를 상대노드의 레벨까지 맞춘다. => log(n)
3. depth 레벨이 맞춰지면, 그 단부터 하나하나 부모를 비교한다. => log(n)
=> 14x14x10000=200만
"""
from collections import deque
import sys
sys.stdin=open("input.txt", "r")
input=sys.stdin.readline

def makeParentINFO():
    return

def makeTreeINFO(): #O(n)
    q=deque([1]) # 루트 노드는 무조건 1
    while q:
        node=q.popleft()
        for x in tree[node]: 
            tree[x].remove(node)
            # parent update
            depth[x]=depth[node]+1
            q.append(x)

def lower_bound(a,b,start,end):    
    while (end-start>0):
        mid=(start+end)//2
        if(a[mid]!=b[mid]):
            start=mid+1
        else:
            end=mid
    return start
        
def lca(a,b):
    #b가 더 깊도록 설정
    depth_num=depth[b]
    if depth[a]>depth[b]: depth_num=depth[a]
    
    
    # 깊이가 같아지도록
    new_b=parent[b][-len(parent[a]):]
    if parent[a]==new_b:
        print(parent[a][0])
    else:
        idx=lower_bound(parent[a],new_b,0,len(new_b)-1)
        print(new_b[idx])
        

n=int(input())
tree=[[]for _ in range(n+1)]
depth=[0]*(n+1)
for idx  in range(n-1):
    s,v=map(int,input().split())
    tree[s].append(v)
    tree[v].append(s)
    
depth[1]=0
makeTreeINFO()
# print(depth)
    
for _  in range(int(input())):
    a,b=map(int,input().split())
    lca(a,b)