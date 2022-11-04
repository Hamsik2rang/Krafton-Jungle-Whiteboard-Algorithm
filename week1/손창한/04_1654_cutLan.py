import sys
input = sys.stdin.readline

k, n = map(int, input().split())
li = list(int(input()) for _ in range(k))

start, end = 1, max(li)
while start <= end:
    mid = (start+end)//2
    cnt = 0

    for l in li:
        cnt += l//mid

    if cnt >= n:
        start = mid+1

    else:
        end = mid-1

print(end)
