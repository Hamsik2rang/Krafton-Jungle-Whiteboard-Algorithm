import sys
input = sys.stdin.readline

# 0< S < 51
S, dot, kes, hong = map(int, input().split())

if (dot + kes + hong) < S : 
    print(0)
    exit(0)

dp = [[[[-1 for _ in range(51)]for __ in range(51)]for ___ in range(51)]for ____ in range(51)]

def song(s, dot, kes, hong) : 
    if s == 0 : 
        if dot == 0 and kes == 0 and hong == 0 : 
            return 1
        else :
            return 0
    
    if (dot < 0) or kes < 0 or hong < 0 : 
        return 0

    if dp[s][dot][kes][hong] != -1 : 
        return dp[s][dot][kes][hong]
    
    dp[s][dot][kes][hong] = 0
    
    for i in range(0, 2) : 
        for j in range(0, 2) : 
            for k in range(0, 2) :
                if (i == 0) and (j == 0) and (k == 0) : 
                    continue
                dp[s][dot][kes][hong] += song(s - 1, dot - i, kes - j, hong - k)
    dp[s][dot][kes][hong] %= 1000000007

    return dp[s][dot][kes][hong]


print(song(S, dot, kes, hong))
    

