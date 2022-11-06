####################현재 수정완료##############################
# 알고리즘 문제가 아니라 로그함수의 문제였음 ㅋㅋㅋㅋㅋㅋ 2시간동안 고민했는데...
# log함수를 typecasting으로 int로 바꾸게되면 가끔 4.99999...가 나와서 k값이 제대로 안나올때가 있다
# int() 가 아니라 반올림함수 round()를 써서 해결했음

import sys
from math import log
input = sys.stdin.readline

N = int(input())
k = round(log(N,3))
# print(k, type(k))

# 3의 지수 k
# N의 몇번째 줄을 뽑을까요 index 
# return : string형태 
def starPowThree(k : int, index : int) : 
    # 초기케이스 설정 
    if k == 0 : 
        return '*'
    else : # k=2일때 4->1->0   k=2일때 5->2->0
        deeperIdx = index % (3**(k-1))
        if index // (3**(k-1)) == 1 : #몫: 현재 자리 찾기 
            return starPowThree(k-1, deeperIdx) + (' ' * (3**(k-1))) + starPowThree(k-1, deeperIdx)
        else : 
            return starPowThree(k-1, deeperIdx) * 3
            
for i in range(0, N) : 
    print(starPowThree(k, i))