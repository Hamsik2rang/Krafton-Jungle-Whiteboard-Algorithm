import sys
input = sys.stdin.readline
from itertools import combinations

# 수열의 크기 N
N = int(input())
S = list(map(int, input().split()))

result = []

# 모든 부분집합을 찾는다 
for n in range(1, N + 1) : 
    c = combinations(S, n)
    result.extend(c)

# 부분집합의 합을 전부 계산한다 
for r in range(len(result)) : 
    result[r] = sum(result[r])
result.sort()

# 1부터 가장 작은 자연수를 찾는다 
ans = 1
for n in range(len(result)) : 
    if ans == result[n] : 
        ans += 1
print(ans)
