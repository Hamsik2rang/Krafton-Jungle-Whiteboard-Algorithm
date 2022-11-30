import sys
input = sys.stdin.readline

# pypy
def row(r, n):
    for i in range(9):
       if brd[r][i] == n:
           return False
    return True

def col(c, n):
    for i in range(9):
       if brd[i][c] == n:
           return False
    return True

def sqr(r, c, n):
    sr = r - (r%3)
    sc = c - (c%3)
    for dr in range(3):
        for dc in range(3):
            if brd[sr+dr][sc+dc] == n:
                return False
    return True

def bt(n):
    if len(chk) == n:
        raise
    for i in range(1, 10):
        r, c = chk[n]
        if row(r, i) and col(c, i) and sqr(r, c, i):
            brd[r][c] = i
            bt(n+1)
            brd[r][c] = 0

brd = []
chk = []
for i in range(9):
    l = list(map(int, input().split()))
    brd.append(l)
    for j in range(9):
        if l[j] == 0:
            chk.append((i, j))
try:
    bt(0)
except:
    for l in brd:
        print(*l)
