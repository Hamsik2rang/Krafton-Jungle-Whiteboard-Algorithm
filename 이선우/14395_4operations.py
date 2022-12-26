import sys

sys.stdin = open("input.txt", "r")

import sys
from collections import deque

def bfs(start):
    visited.append(start_num)
    q = deque()
    q.append([start, ''])
    
    while q:
        num, result = q.popleft()

        if num == end_num:
            return result

        for operation in ['*', '+', '/']:
            if operation == '*':
                temp = num * num
            elif operation == '+':
                temp = num + num
            else:
                temp = 1

            if temp <= end_num and temp not in visited:
                visited.append(temp)
                q.append([temp, result + operation])
    else:
        return -1

start_num, end_num = map(int, sys.stdin.readline().split(' '))
visited = []

if start_num == end_num:
    print(0)
else:
    print(bfs(start_num))
    
"""
# 문제처럼 s,t가 주어졌을 때, s에서 *,+만을 이용해서 t에 도달할 수 있고(case 1)
# 동시에 s를 '/'를 이용해서 1로 만든 다음에도 t를 도달 할 수 있다고 하면(Case 2),
# case 1에서의 최적의 답(최소연산 + 사전순 맨위)을 A라고 하고
# case 2에서의 최적의 답을 B라고 할때
# A가 항상 B보다 더 최적이다라고 보장 할 수 없습니다.

def bfs(start):
    visited.append(start_num)
    q = deque()
    q.append([start, ''])
    
    while q:
        num, result = q.popleft()

        if num == end_num:
            return result

        for operation in ['*', '+']:
            if operation == '*':
                temp = num * num
            else:
                temp = num + num

            if temp <= end_num and temp not in visited:
                visited.append(temp)
                q.append([temp, result + operation])
    else:
        print(-1)
        exit()

start_num, end_num = map(int, sys.stdin.readline().split(' '))
visited = []

if start_num == end_num:
    print(0)
elif end_num == 0:
    print('-')
elif (end_num % start_num) != 0:
    print('/', bfs(1), sep='')
else:
    print(bfs(start_num))
"""