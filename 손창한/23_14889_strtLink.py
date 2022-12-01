import sys
from itertools import combinations
input = sys.stdin.readline

# # pypy
# n = int(input())
# graph = list(list(map(int, input().split())) for _ in range(n))
# plyr = [i for i in range(n)]
# dif = sys.maxsize
# 
# for strt in combinations(plyr, n//2):
#     link = list(set(plyr) - set(strt))
#     p, s = 0, 0
#     for i in range(n//2):
#         for j in range(n//2):
#             if i == j:
#                 continue
#             p += graph[strt[i]][strt[j]]
#             s += graph[link[i]][link[j]]
#     dif = min(dif, abs(p - s))
# print(dif)

# python
n = int(input())
graph = list(list(map(int, input().split())) for _ in range(n))
dl = []
for team in combinations(range(n), n//2):
    tmp = 0
    for i, j in combinations(team, 2):
        tmp += graph[i][j] + graph[j][i]
    dl.append(tmp)
dif = sys.maxsize
for i in range(len(dl)//2):
    dif = min(dif, abs(dl[i] - dl[-i-1]))
print(dif)
