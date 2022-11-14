import sys
from collections import deque
input = sys.stdin.readline

def check_prime():
    for i in range(2, 100):
        if prime_list[i]:
            for j in range(2*i, 10000, i):
                prime_list[j] = False

def bfs(s, e):
    queue = deque()
    queue.append([s, 0])
    vis = [False] * 10000
    vis[s] = True
    while queue:
        cur, cnt = queue.popleft()
        if cur == e:
            return cnt
        for i in range(4):
            for j in range(10):
                tmp = int(str(cur)[:i] + str(j) + str(cur)[i+1:])
                if not vis[tmp] and prime_list[tmp] and 1000 <= tmp:
                    vis[tmp] = True
                    queue.append([tmp, cnt+1])
    return "Impossible"

prime_list = [True] * 10000
check_prime()
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(bfs(a, b))
