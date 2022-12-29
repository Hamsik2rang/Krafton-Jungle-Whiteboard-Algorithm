'''
1. 문제의 시간 제한은?
5초

2. 문제의 최대 N값은?(항상 N이 아닐 수도 있으며, 여러 개일 수도 있음)
1,000,000

3. 1, 2를 바탕으로 이 문제에서 허용하는 최대 시간 복잡도는?
NlogN

4. 3을 바탕으로 문제를 읽었을 때 사용할 수 있는 알고리즘은?


5. 왜 4라고 생각했는가?

1) 주가 중 가장 높은 애를 고른다.
2) 그 앞 애들을 전부 구매하고, 가장 높은 데에서 파는 걸로 가정해서 이익금 계산
3) 가장 높은 애까지를 없앤다
4) list 빌때까지 반복한다
'''

import heapq
import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    total = 0
    nums = range(n)
    stocks = list(map(lambda x:(-int(x)), input().split()))
    while(stocks):
        heapStock = list.copy(stocks)
        heapq.heapify(heapStock)
        max = -heapq.heappop(heapStock)
        idx = stocks.index(-max)
        for minus in stocks[:idx]:
            money = -minus
            total += (max - money)
        if idx == len(stocks)-1:
            break
        stocks = stocks[idx+1:]
    print(total)