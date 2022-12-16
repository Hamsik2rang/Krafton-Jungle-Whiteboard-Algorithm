import sys
input = sys.stdin.readline

n, k = map(int, input().split())
l = list(int(input()) for _ in range(n))

start = min(l)
end = start + k
ret = 0
while start <= end:
    mid = (start+end)//2
    tmp = 0
    for x in l:
        if mid > x:
            tmp += mid - x
    if tmp <= k:
        start = mid+1
        ret = max(ret, mid)
    else:
        end = mid-1
print(ret)
