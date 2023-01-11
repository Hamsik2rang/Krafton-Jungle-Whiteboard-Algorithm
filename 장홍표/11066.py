'''
1. 문제의 시간 제한은?
2초
2. 문제의 최대 N값은?(항상 N이 아닐 수도 있으며, 여러 개일 수도 있음)
499! = 2.44 * 10^1131
3. 1, 2를 바탕으로 이 문제에서 허용하는 최대 시간 복잡도는?
logN = ca. 1131
4. 3을 바탕으로 문제를 읽었을 때 사용할 수 있는 알고리즘은?
그리디 or DP
5. 왜 4라고 생각했는가?
완전탐색 시 너무 많은시간이 걸림 + 큰수는 최대한 적은수로 더해야 함
'''
import sys; input = sys.stdin.readline
import copy
from collections import deque

T = int(input().strip())

for _ in range(T):
    K = int(input().strip())
    cost = 0
    array = list(map(int, input().strip().split()))
    while(len(array)!=1):
        minpos = array.index(min(array))
        if(minpos==0):
            t = array[minpos+1]
            array.pop(minpos+1)
            array[minpos] += t
            cost += array[minpos]
        elif(minpos==len(array)-1):
            t = array[minpos-1]
            array.pop(minpos-1)
            array[minpos-1] += t
            cost += array[minpos-1]
        elif(array[minpos+1] > array[minpos-1]):
            t = array[minpos-1]
            array.pop(minpos-1)
            array[minpos-1] += t
            cost += array[minpos-1]
        else:
            t = array[minpos+1]
            array.pop(minpos+1)
            array[minpos] += t
            cost += array[minpos]
    print(cost)
    
# 그리디 알고리즘 != 정답 다만, 최솟값에 근접