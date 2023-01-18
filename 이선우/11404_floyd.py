import sys

sys.stdin = open("input.txt", "r")

import sys

city_count = int(sys.stdin.readline())
bus_count = int(sys.stdin.readline())
max = 100_001
bus_cost = [[max for _ in range(city_count + 1)] for _ in range(city_count + 1)]

for _ in range(bus_count):
    start, end, cost = map(int, input().split())
    bus_cost[start][end] = min(cost, bus_cost[start][end])

for k in range(1, city_count + 1):
    for r in range(1, city_count + 1):
        for c in range(1, city_count + 1):
            if r == c:
                bus_cost[r][c] = 0 
            else:
                bus_cost[r][c] = min(bus_cost[r][c], bus_cost[r][k] + bus_cost[k][c])

for r in bus_cost[1:]:
    for c in r[1:]:
        if c == max:
            print(0, end = " ")
        else:
            print(c, end = " ")
    print()