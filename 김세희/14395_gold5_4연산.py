'''
1. 문제의 시간 제한은?
2초

2. 문제의 최대 N값은?(항상 N이 아닐 수도 있으며, 여러 개일 수도 있음)
10^9(10억)

3. 1, 2를 바탕으로 이 문제에서 허용하는 최대 시간 복잡도는?
OlogN

4. 3을 바탕으로 문제를 읽었을 때 사용할 수 있는 알고리즘은?
BFS

5. 왜 4라고 생각했는가?
E가 logN개가 됨
'''

from collections import deque
s, t = map(int, input().split())

togo = deque([(s,t,"")])
visited = []

if s==t:
    print(0)
    exit()

def find(now, goal, answer):
    if 1 in visited and now>goal:
        return
    if now==goal:
        print(answer)
        exit()
    if goal==0:
        print("-")
        exit()
    if now*now not in visited:
        visited.append(now*now)
        togo.append((now*now, goal, answer+"*"))
    if now+now not in visited:
        visited.append(now+now)
        togo.append((now+now, goal, answer+"+"))
    if 1 not in visited:
        visited.append(1)
        togo.append((1, goal, answer+"/"))

while(togo):
    now, goal, answer = togo.popleft()
    find(now, goal, answer)

print(-1)