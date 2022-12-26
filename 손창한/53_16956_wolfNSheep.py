import sys
input = sys.stdin.readline

R, C = map(int, input().split())
ranch = [[] for _ in range(R)]
for i in range(R):
    ranch[i].extend(input().rstrip())
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# if S, W adj: flg on
flg = False
for r in range(R):
    for c in range(C):
        if ranch[r][c] == 'W':
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if -1<nr<R and -1<nc<C:
                    if ranch[nr][nc] == 'S':
                        flg = True
                        break
if flg:
    print(0)
else:
    print(1)
    for r in range(R):
        for c in range(C):
            if ranch[r][c] == '.':
                ranch[r][c] = 'D'
    for l in ranch:
        print(*l, sep='')
