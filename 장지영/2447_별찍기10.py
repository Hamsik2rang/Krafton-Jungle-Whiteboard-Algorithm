import sys
from math import log
input = sys.stdin.readline

N = int(input())
k = int(log(N,3))

# 3의 지수 k
# N의 몇번째 줄을 뽑을까요 index 
# return : string형태 
def starPowThree(k : int, index : int) : 
    # 초기케이스 설정 
    if k == 0 : 
        return '*'
    else : # k=2일때 4->1->0   k=2일때 5->2->0
        deeperIdx = index % (3**(k-1)) #나머지 : 재귀돌릴 때 자리찾기용
        if index // (3**(k-1)) == 1 : #몫: 현재 자리 찾기 
            return starPowThree(k-1, deeperIdx) + (' ' * 3**(k-1)) + starPowThree(k-1, deeperIdx)
        else : 
            return starPowThree(k-1, deeperIdx) * 3
            
for i in range(0, N) : 
    print(starPowThree(k, i))