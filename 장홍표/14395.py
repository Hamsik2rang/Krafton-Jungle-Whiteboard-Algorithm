import sys
from collections import deque
input = sys.stdin.readline
dq = deque()
flag = 1

s, t = map(int, input().strip().split())

if(s==t):
    print('0')
elif(t==1):
    print('/')
elif(t==0):
    print('-')
else:
    dq.append(['*',s])
    dq.append(['+',s])
    dq.append(['/',s])
    while(dq):
        elem, value = dq.popleft()
        lastelem = elem[-1]
        value =  eval(str(value) + lastelem + str(value))
        if(value == t):
            print(elem)
            flag =0
            break
        elif(value <= 10e9 and value < t):
            if(value != 1):
                dq.append([elem + '*',value])
            dq.append([elem + '+',value])
    if(flag ==1):
        print(-1)