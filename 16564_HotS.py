import sys

sys.stdin = open("input.txt", "r")

import sys

iter, goal = map(int, sys.stdin.readline().split())
lvl_list = [int(sys.stdin.readline()) for _ in range(iter)]

min_lvl = min(lvl_list)
max_lvl = min_lvl + goal
ans = 0

def check(lvl_list: list, lvl_cutoff: int, goal: int):
    lvl_total = 0

    for lvl in lvl_list:
        if lvl < lvl_cutoff:
            lvl_total += lvl_cutoff - lvl
    if lvl_total <= goal:
        return True
    else:
        return False

while min_lvl <= max_lvl:
    mid = (min_lvl + max_lvl) // 2
    if check(lvl_list, mid, goal):
        min_lvl = mid + 1
        ans = max(ans, mid)
    else:
        max_lvl = mid - 1

print(ans)