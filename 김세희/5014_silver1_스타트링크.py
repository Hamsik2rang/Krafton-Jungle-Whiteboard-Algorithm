'''
bfs로 푼다.
'''

from collections import deque

top, now, goal, up, down = map(int, input().split())
ans = -1

visited = [False] * (top+1)
bp = [int(1e9)]*(top+1)

queue = deque([now])
bp[now] = 0

while(queue):
    floor = queue.popleft()
    if floor == goal:
        ans = bp[floor]
        break

    nextFloors = [floor-down, floor+up]
    
    for next in nextFloors:
        if 1<=next<=top and not visited[next]:
            visited[next] = True
            bp[next] = min(bp[next], bp[floor] + 1)
            queue.append(next)

if ans>=0:
    print(ans)
else:
    print("use the stairs")