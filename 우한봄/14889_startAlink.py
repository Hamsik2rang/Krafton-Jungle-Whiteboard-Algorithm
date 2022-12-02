import sys
input=sys.stdin.readline

def sumScore(lst):
    score=0
    for i in lst:
        for j in lst:
            if i!=j:
                score+=mapp[i][j]
    
    return score
                 
    
def dfs():
    # 원소 1 선택
    # 원소 2 선택
    # 원소 3 선택
    # score 비교
    # 최소면 업데이트
    return
           
n=int(input().split())
mapp=[list(map(int,input().split())) for _ in range(4)]

minAns = float('Inf')
start=[]
link=[]
