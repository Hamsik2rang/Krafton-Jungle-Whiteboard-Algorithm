import sys
input = sys.stdin.readline

x, y, c = map(float, input().split())
start, end = 1, min(x, y)
err = .001

while start + err < end:
    mid = (start+end)/2
    h1 = (x**2 - mid**2)**.5
    h2 = (y**2 - mid**2)**.5
    tmp = (h1 * h2) / (h1 + h2)
    if tmp >= c:
        start = mid
    else:
        end = mid
print(end)
