import sys
input = sys.stdin.readline
#HOTS Progamer - 시간초과

N, Level = map(int, input().strip().split())
LvArr = []
for _ in range(N):
    LvArr.append(int(input()))

LvArr.sort()
while(Level):
    LvArr[0] += 1
    LvArr.sort()
    Level -= 1
print(min(LvArr))