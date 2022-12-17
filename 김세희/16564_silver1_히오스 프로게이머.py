import sys
input = sys.stdin.readline

teams = []
n, k = map(int, input().split())

for _ in range(n):
    teams.append(int(input()))

start = min(teams)
end = 2_000_000_000
result = start

while(True):
    if start>end:
        break
    half = (start+end)//2
    temp = 0
    for i in range(n):
        if teams[i]<half:
            temp+=half-teams[i]
    if temp<=k:
        start = half+1
        result = half
    elif temp>k:
        end = half-1  

print(result)