import sys
input = sys.stdin.readline

n = int(input())

def isPrime(x):
    if not x%2:
        return False
    for i in range(3, int(x**.5)+1, 2):
        if not x%i:
            return False
    return True

dp = [[] for _ in range(n)]
dp[0].extend([2, 3, 5, 7])
for cnt in range(1, n):
    for i in dp[cnt-1]:
        for j in [1, 3, 5, 7, 9]:
            tmp = i*10 + j
            if isPrime(tmp):
                dp[cnt].append(tmp)
print(*dp[-1], sep='\n')
