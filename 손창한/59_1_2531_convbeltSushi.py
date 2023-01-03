import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().rsplit())
arr = [int(input().rstrip()) for _ in range(n)]
lp, rp = 0, 0
cnt = 0

while lp < n:
    rp = lp + k # range: lp ~ rp-1
    dif = set() # how many kinds of
    flg = True # if coupon used? false : true
    for i in range(lp, rp):
        i %= n
        dif.add(arr[i])
        if arr[i] == c:
            flg = False
    tmp = len(dif)
    if flg:
        tmp += 1
    cnt = max(cnt, tmp)
    lp += 1
print(cnt)