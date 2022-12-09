import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

def bfs(start):
    queue = deque()
    queue.append((start, 0))
    visited = [False] * (f+1)
    visited[start] = True
    
    while queue:
        res, cnt = queue.popleft()

        if res == g:
            return cnt

        for x in ('u', 'd'):
            new = res + u if x == 'u' else res - d
            if 1 <= new <= f and not visited[new]:
                queue.append((new, cnt + 1))
                visited[new] = True

    return "use the stairs"

f, s, g, u, d = map(int, input().split())
print(bfs(s))


