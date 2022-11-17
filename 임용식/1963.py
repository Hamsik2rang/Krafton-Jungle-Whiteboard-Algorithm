import sys
from collections import deque


def bfs(a: str, b: str) -> int:
    q = deque()
    check = [False for _ in range(10000)]
    q.append((a, 0))
    while len(q) > 0:
        cur_string, cur_count = q.popleft()
        if cur_string == b:
            return cur_count

        for digit in range(4):
            for num in range(1 if digit == 0 else 0, 10):
                if num == int(cur_string[digit]):
                    continue
                next_int = int(
                    str(cur_string[:digit] + str(num) + cur_string[digit + 1 :])
                )

                if is_prime[next_int] and not check[next_int]:
                    check[next_int] = True
                    q.append((str(next_int), cur_count + 1))
    return "Impossible"


is_prime = [False for _ in range(10000)]
is_checked_number = [False for _ in range(10000)]

for i in range(2, 10000):
    if not is_checked_number[i]:
        is_prime[i] = True
        for j in range(i * 2, 10000, i):
            is_checked_number[j] = True

t = int(sys.stdin.readline())
while t > 0:
    t -= 1

    a, b = sys.stdin.readline().split()
    answer = bfs(a, b)
    print(answer)
