import sys

sys.stdin = open("input.txt", "r")

import sys
from collections import deque

def is_prime(n: int):
    if n == 1:
        return False
    else:
        for i in range(2,n):
            if (n%i) == 0:
                return False
        return True

def bfs(start: int, goal: int):
    queue = deque()
    visited = [0] * 10001
    queue.append(start)
    visited[start] = 0

    while queue:
        current_num = str(queue.popleft())
        if int(current_num) == goal:
            return visited[goal]

        for digit in range(4):
            for num in range(10): 
                new_num = int(current_num[:digit] + str(num) + current_num[digit + 1:])

                if new_num < 1000 or new_num == int(current_num):
                    continue
                else:
                    if not visited[new_num] and new_num in prime_list:
                        queue.append(new_num)
                        visited[new_num] = visited[int(current_num)] + 1

prime_list = []

for num in range(1000, 10001):
    if is_prime(num):
        prime_list.append(num)

iter = int(sys.stdin.readline())
ans = []

for _ in range(iter):
    start, goal = map(int, sys.stdin.readline().split())
    ans.append(bfs(start, goal))

for path in ans:
    if path == None:
        print("Impossible")
    else:
        print(path)

