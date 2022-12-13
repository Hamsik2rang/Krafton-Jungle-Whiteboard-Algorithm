import sys

sys.setrecursionlimit(10**6)


def solution(x: int, y: int, z: int) -> int:
    x = 0 if x < 1 else x
    y = 0 if y < 1 else y
    z = 0 if z < 1 else z
    if memo[x][y][z]:
        return memo[x][y][z]

    if x == 0 and y == 0 and z == 0:
        return 0
    memo[x][y][z] = float("inf")
    if x < 1 and y >= 1 and z >= 1:
        memo[x][y][z] = min(
            memo[x][y][z], solution(x, y - 9, z - 3) + 1, solution(x, y - 3, z - 9) + 1
        )
    elif y < 1 and x >= 1 and z >= 1:
        memo[x][y][z] = min(
            memo[x][y][z], solution(x - 9, y, z - 3) + 1, solution(x - 3, y, z - 9) + 1
        )
    elif z < 1 and x >= 1 and y >= 1:
        memo[x][y][z] = min(
            memo[x][y][z], solution(x - 9, y - 3, z) + 1, solution(x - 3, y - 9, z) + 1
        )
    elif x < 1 and y < 1 and z >= 1:
        memo[x][y][z] = min(memo[x][y][z], solution(x, y, z - 9) + 1)
    elif x < 1 and y >= 1 and z < 1:
        memo[x][y][z] = min(memo[x][y][z], solution(x, y - 9, z) + 1)
    elif x >= 1 and y < 1 and z < 1:
        memo[x][y][z] = min(memo[x][y][z], solution(x - 9, y, z) + 1)
    else:
        memo[x][y][z] = min(
            memo[x][y][z],
            solution(x - 9, y - 3, z - 1) + 1,
            solution(x - 9, y - 1, z - 3) + 1,
            solution(x - 3, y - 9, z - 1) + 1,
            solution(x - 1, y - 9, z - 3) + 1,
            solution(x - 3, y - 1, z - 9) + 1,
            solution(x - 1, y - 3, z - 9) + 1,
        )
    return memo[x][y][z]


n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
while len(lst) < 3:
    lst.append(0)
a, b, c = lst
memo = [[[0 for _ in range(61)] for _ in range(61)] for _ in range(61)]
print(solution(a, b, c))
