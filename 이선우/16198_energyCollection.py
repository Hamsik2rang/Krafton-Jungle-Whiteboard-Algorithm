import sys

sys.stdin = open("input.txt", "r")

import sys

ball_count = int(sys.stdin.readline())
balls = list(map(int, sys.stdin.readline().split()))
ans = 0

def check(ball_list, total):
    global ans
    if len(ball_list) == 2:
        ans = max(ans, total)
        return

    for ball in range(1, len(ball_list)-1):
        check(ball_list[:ball] + ball_list[ball + 1:], total + (ball_list[ball - 1] * ball_list[ball + 1]))


check(balls, 0)
print(ans)