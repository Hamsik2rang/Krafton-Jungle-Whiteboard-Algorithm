'''
1. 문제의 시간 제한은?
1초

2. 문제의 최대 N값은?(항상 N이 아닐 수도 있으며, 여러 개일 수도 있음)
100

3. 1, 2를 바탕으로 이 문제에서 허용하는 최대 시간 복잡도는?
ON^2 가능

4. 3을 바탕으로 문제를 읽었을 때 사용할 수 있는 알고리즘은?
DFS

5. 왜 4라고 생각했는가?
다음 수를 지정하는 dfs함수를 하나 만들고, 각 자릿수마다 돌리면서 호출해 주면 될 것 같음
시간초과
dfs하면 2^n되는듯
---
dp와 비슷한 양상을 보인다
- 수를 확인해 보면 9, 17, 32, 61, 116, 222, 424
각각 이전 수*2보다 1, 2, 3, 6, 10, 20씩 감소하고 있음
이 감소하는 값은 이전 수 중에서 0 혹은 9로 끝난 수의 개수

각 경우의 수마다 전체 dfs를 구하지 않고,
0부터 9까지의 수로 끝나는 경우의 카운트를 담는 배열을 생성
이전값의 배열을 참고해서 0 혹은 9로 끝난 수의 개수를 구하고 이걸 이전수*2에서 빼서 구하기
'''
import sys
sys.setrecursionlimit(10**7)

n = int(input())
dp = [0]*(n+1)
dp[0] = 0
dp[1] = 9
last = [0,1,1,1,1,1,1,1,1,1]

if n<=1:
    print(dp[n])
    exit()

for idx in range(2,n+1):
    dp[idx] = (dp[idx-1] * 2 - last[0] - last[9])%1000000000
    newLast = last.copy()
    for i in range(10):
        if 0<i<9:
            newLast[i] = last[i-1]+last[i+1]
        elif i==0:
            newLast[i] = last[i+1]
        else:
            newLast[i] = last[i-1]
    last = newLast


print(dp[n])