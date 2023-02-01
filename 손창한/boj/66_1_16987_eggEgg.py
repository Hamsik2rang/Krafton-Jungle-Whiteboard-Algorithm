import sys
input = sys.stdin.readline

n = int(input())
egg = list(list(map(int, input().split())) for _ in range(n))
cnt = 0

def chk(egg):
    cnt = 0
    for e in egg:
        if e[0] <= 0:
            cnt += 1
    return cnt

def dfs(idx):
    global cnt
    # escape
    if idx == n:
        cnt = max(cnt, chk(egg))
        return
    if egg[idx][0] <= 0:
        dfs(idx+1)
    else:
        flg = True
        for i in range(len(egg)):
            if i != idx and egg[i][0] > 0:
                flg = False
                egg[idx][0] -= egg[i][1]
                egg[i][0] -= egg[idx][1]
                dfs(idx+1)
                egg[idx][0] += egg[i][1]
                egg[i][0] += egg[idx][1]
        if flg:
            dfs(n)

dfs(0)
print(cnt)