import sys
input = sys.stdin.readline
from collections import deque

N = int(input().strip())
q = deque()
answer = []
for _ in range(N):
    cmd = input().strip().split()
    if(cmd[0] == 'push'):
        q.append(cmd[1])
    elif(cmd[0]=='pop'):
        try:
            print(q.popleft())
        except:
            print('-1')
    elif(cmd[0]=='size'):
        print(len(q))
    elif(cmd[0]=='empty'):
        if(len(q)==0):
            print('1')
        else:
            print('0')
    elif(cmd[0]=='front'):
        try:
            print(q[0])
        except:
            print('-1')
    elif(cmd[0]=='back'):
        try:
            print(q[-1])
        except:
            print('-1')