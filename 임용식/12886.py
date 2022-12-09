import sys
from collections import deque

a, b, c = map(int, sys.stdin.readline().split())
sum = a + b + c

if sum % 3 != 0:
    print(0)
    exit(0)

check = [[False for _ in range(sum + 1)] for _ in range(sum + 1)]

q = deque()
q.append([a, b, c])
check[a][b] = True
answer = False
while q:
    ca, cb, cc = q.popleft()

    if ca == cb and cb == cc:
        answer = True
        break

    if ca > cb and not check[ca - cb][cb + cb]:
        check[ca - cb][cb + cb] = True
        q.append((ca - cb, cb + cb, cc))
    if ca < cb and not check[ca + ca][cb - ca]:
        check[ca + ca][cb - ca] = 1
        q.append((ca + ca, cb - ca, cc))
    if cb > cc and not check[cb - cc][cc + cc]:
        check[cb - cc][cc + cc] = 1
        q.append((ca, cb - cc, cc + cc))
    if cb < cc and not check[cb + cb][cc - cb]:
        check[cb + cb][cc - cb] = 1
        q.append((ca, cb + cb, cc - cb))
    if cc > ca and not check[ca + ca][cc - ca]:
        check[ca + ca][cc - ca] = 1
        q.append((ca + ca, cb, cc - ca))
    if cc < ca and not check[ca - cc][cc + cc]:
        check[ca - cc][cc + cc] = 1
        q.append((ca - cc, cb, cc + cc))

print(1 if answer else 0)
