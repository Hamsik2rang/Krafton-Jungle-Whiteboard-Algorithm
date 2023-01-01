import sys

sys.stdin = open("input.txt", "r")

import sys

def dfs(start):
    if len(sublist) == sublist_length:
        ans.add(tuple(sublist))
        return

    for num in range(start, iter):
        sublist.append(num_list[num])
        dfs(num + 1)
        sublist.pop()

iter, sublist_length = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
sublist, ans = [], set()
num_list.sort()

dfs(0)
for set in sorted(list(ans)):
    print(*set)