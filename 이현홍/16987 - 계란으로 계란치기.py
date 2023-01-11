import sys

N = int(sys.stdin.readline())
if N == 1:
    print(0)
    exit()
durabilitys = []
weights = []
for _ in range(N):
    d, w = map(int, sys.stdin.readline().split())
    durabilitys.append(d)
    weights.append(w)

mx = 0


def DFS(turn=0, count=0):
    global mx
    if turn == N:
        mx = max(mx, count)
    else:
        if (N - turn) * 2 + count <= mx:
            return
        if durabilitys[turn] <= 0:
            DFS(turn + 1, count)
        else:
            for target in range(N):
                if target == turn:
                    continue
                elif durabilitys[target] <= 0:
                    DFS(turn + 1, count)
                else:
                    ncount = count
                    durabilitys[target] -= weights[turn]
                    durabilitys[turn] -= weights[target]
                    if durabilitys[target] <= 0:
                        ncount += 1
                    if durabilitys[turn] <= 0:
                        ncount += 1
                    DFS(turn + 1, ncount)
                    durabilitys[target] += weights[turn]
                    durabilitys[turn] += weights[target]


DFS()
print(mx)
