import sys
input = sys.stdin.readline
#여러분의 다리가 되어 드리겠습니다!

N = int(input())
ck = [0 for i in range(N+1)]

for _ in range(N-2):
    a, b = map(int, input().strip().split())
    ck[a] = a
    ck[b] =ck[a]
print(ck)