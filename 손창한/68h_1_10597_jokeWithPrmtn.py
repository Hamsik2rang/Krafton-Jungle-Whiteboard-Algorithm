import sys
input = sys.stdin.readline

seq = input().rstrip()
que = []
vis = [False] * 51

def bt(idx):
    # escape
    if idx == len(seq):
        # find max in str arr: 184ms
        # mx = 0
        # for i in que:
        #     mx = max(mx, int(i))
        # if mx == len(que):
        #     print(*que)
        #     exit()
        # find max in int arr: 188ms
        if max(que) == (len(seq)-9)//2 + 9:
            print(*que)
            exit()
    # 1 digit number
    if idx < len(seq) and int(seq[idx]) < 51 and not vis[int(seq[idx])]:
        vis[int(seq[idx])] = True
        # que.append(seq[idx])
        que.append(int(seq[idx]))
        bt(idx+1)
        vis[int(seq[idx])] = False
        que.pop()
    # 2 digits number
    if idx+1 < len(seq) and int(seq[idx:idx+2]) < 51 and not vis[int(seq[idx:idx+2])]:
        vis[int(seq[idx:idx+2])] = True
        # que.append(seq[idx:idx+2])
        que.append(int(seq[idx:idx+2]))
        bt(idx+2)
        vis[int(seq[idx:idx+2])] = False
        que.pop()

bt(0) if len(seq) > 9 else print(*seq)