import sys
from collections import deque
N, M = map(int, sys.stdin.readline().strip().split())

#단, 하나만 떨어져야 함. 두 개가 동시에 떨어지면 안 됨.
coin_map = [[] for _ in range(N)]

for i in range(N):
    coin_map[i] = list(sys.stdin.readline().strip())

# searching coin's position
coin_pos = []

for i in range(N):
    for j in range(M):
        if coin_map[i][j] == 'o':
            coin_pos.append((i,j))

coin_pos_1 = coin_pos[0]
coin_pos_2 = coin_pos[1]
# searching done

q = deque()

# Check out both are at wall
def isWall(x1, y1, x2, y2):
    #1. both wall, 2. both are NOT wall, 3. only one at wall
    if coin_map[x1][y1]=='#' and coin_map[x2][y2]=='#':
        return 'both'
    if coin_map[x1][y1]=='#':
        return (x1,y1)
    if coin_map[x2][y2]=='#':
        return (x2,y2)
    return 'none'

# Check out both coins are out of map
def isOutofMap(x1, y1, x2, y2):
    if (x1<0 or x1>=N or y1<0 or y1>=M) and (x2<0 or x2>=N or y2<0 or y2>=M):
        return 'both'
    if (x1<0 or x1>=N or y1<0 or y1>=M):
        return (x1,y1)
    if (x2<0 or x2>=N or y2<0 or y2>=M):
        return (x2,y2)
    return 'none'


def bfs(x1, y1, x2, y2):
    global q
    q.append((x1, y1, x2, y2))
    steps = 0

    while q:
        steps += 1
        if steps > 10:
            return -1
        
        for _ in range(len(q)):
            cx1, cy1, cx2, cy2 = q.popleft()
            for (dx, dy) in [(-1,0), (0,-1), (1,0), (0,1)]:
                nx1 = cx1 + dx
                ny1 = cy1 + dy
                nx2 = cx2 + dx
                ny2 = cy2 + dy
                outFlag = isOutofMap(nx1, ny1, nx2, ny2)

                #if two coins overlapped, never success
                if nx1 == nx2 and ny1 == ny2:
                    continue
                #both are out of map, fail
                if outFlag == 'both':
                    continue
                elif outFlag == 'none':

                    wallFlag = isWall(nx1, ny1, nx2, ny2)
                    
                    if wallFlag == 'both':
                        continue
                    elif wallFlag == 'none':
                        q.append((nx1, ny1, nx2, ny2))
                    else:
                        if wallFlag == (nx1, ny1):
                            q.append((nx1-dx, ny1-dy, nx2, ny2))
                        else:
                            q.append((nx1, ny1, nx2-dx, ny2-dy))
                else:
                    return steps

answer = bfs(coin_pos_1[0], coin_pos_1[1], coin_pos_2[0], coin_pos_2[1])
# print(answer)
# 동전들이 벽들에 의해 아예 움직일 수 없는 상황에는 queue에 더이상 코인들이 들어가지 않음.
# 그러면 함수의 return 값이 없이 끝남
# 따라서 답 출력할 때 예외처리하는 방법을 선택했음
if not answer:
    print (-1)
else:
    print(answer)
