import sys

T = int(sys.stdin.readline().strip()) #test case

results = []

for _ in range(T):
    K = int(sys.stdin.readline().strip()) # 3~500장. 너무 큼. ~약 500!
    programs = ( list(map(int, sys.stdin.readline().strip().split())) ) # ~10,000

    sum = [0] * (K+1)
    dp = [[0] * (K+1) for i in range(K+1)]

    for i in range(K):
        sum[i+1] = sum[i] + programs[i]
    
    for j in range(1,K):
        for k in range(1,K-j+1):
            dp[k][k+j]=1e9
            for l in range(k, k+j):
                dp[k][k+j] = min(dp[k][k+j], dp[k][l]+dp[l+1][k+j]+sum[k+j]-sum[k-1])
    results.append(dp[1][K])

    # 함수 구현: dp -> 5,000,000
    ###########
for i in range(len(results)):
    print(results[i])

