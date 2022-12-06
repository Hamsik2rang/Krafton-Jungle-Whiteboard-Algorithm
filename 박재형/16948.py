import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline().strip())
r_s, c_s, r_f, c_f = map(int, sys.stdin.readline().split())

#make visited list
visit = [[0 for _ in range(N)] for _ in range(N)]

def bfs(r1,c1,r2,c2):
    q = deque()
    q.append((r1,c1,0))

    while len(q) > 0:
        r, c, cur_count = q.popleft()

        dr = [-2, -2, 0, 0, 2, 2]
        dc = [-1, 1, -2, 2, -1, 1]
        
        for i in range(6):
            nr = r + dr[i]
            nc = c + dc[i]

            if (
                nr >= 0
                and nr <= N-1
                and nc >= 0
                and nc <= N-1
            ):
                if nr == r2 and nc == c2:
                    return cur_count+1
                if visit[nr][nc] == 0:
                    visit[nr][nc] = 1
                    q.append((nr, nc, cur_count+1))
    return -1

print(bfs(r_s, c_s, r_f, c_f))
