import sys

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, sys.stdin.readline().split()))

answer = 0

for r in range(n):
    for c in range(m):
        # ■□□□
        if c >= 0 and c + 3 < m:
            answer = max(
                answer,
                graph[r][c] + graph[r][c + 1] + graph[r][c + 2] + graph[r][c + 3],
            )
        # ■
        # □
        # □
        # □
        if r >= 0 and r + 3 < n:
            answer = max(
                answer,
                graph[r][c] + graph[r + 1][c] + graph[r + 2][c] + graph[r + 3][c],
            )
        # ■□
        # □□
        if r >= 0 and r + 1 < n and c >= 0 and c + 1 < m:
            answer = max(
                answer,
                graph[r][c] + graph[r][c + 1] + graph[r + 1][c] + graph[r + 1][c + 1],
            )
        #  □
        # ■□□
        if r >= 0 and r + 1 < n and c >= 0 and c + 2 < m:
            answer = max(
                answer,
                graph[r + 1][c]
                + graph[r + 1][c + 1]
                + graph[r + 1][c + 2]
                + graph[r][c + 1],
            )
        # ■
        # □□
        # □
        if r >= 0 and r + 2 < n and c >= 0 and c + 1 < m:
            answer = max(
                answer,
                graph[r][c] + graph[r + 1][c] + graph[r + 1][c + 1] + graph[r + 2][c],
            )
        # ■□□
        #  □
        if r >= 0 and r + 1 < n and c >= 0 and c + 2 < m:
            answer = max(
                answer,
                graph[r][c] + graph[r][c + 1] + graph[r][c + 2] + graph[r + 1][c + 1],
            )
        #  ■
        # □□
        #  □
        if r >= 0 and r + 2 < n and c - 1 >= 0 and c < m:
            answer = max(
                answer,
                graph[r][c] + graph[r + 1][c] + graph[r + 2][c] + graph[r + 1][c - 1],
            )
        # ■
        # □□
        #  □
        if r >= 0 and r + 2 < n and c >= 0 and c + 1 < m:
            answer = max(
                answer,
                graph[r][c]
                + graph[r + 1][c]
                + graph[r + 1][c + 1]
                + graph[r + 2][c + 1],
            )
        #  □□
        # ■□
        if r - 1 >= 0 and r < n and c >= 0 and c + 2 < m:
            answer = max(
                answer,
                graph[r][c]
                + graph[r][c + 1]
                + graph[r - 1][c + 1]
                + graph[r - 1][c + 2],
            )
        #  ■
        # □□
        # □
        if r >= 0 and r + 2 < n and c - 1 >= 0 and c < m:
            answer = max(
                answer,
                graph[r][c]
                + graph[r + 1][c]
                + graph[r + 1][c - 1]
                + graph[r + 2][c - 1],
            )
        # ■□
        #  □□
        if r >= 0 and r + 1 < n and c >= 0 and c + 2 < m:
            answer = max(
                answer,
                graph[r][c]
                + graph[r][c + 1]
                + graph[r + 1][c + 1]
                + graph[r + 1][c + 2],
            )

        # ■
        # □
        # □□
        if r >= 0 and r + 2 < n and c >= 0 and c + 1 < m:
            answer = max(
                answer,
                graph[r][c] + graph[r + 1][c] + graph[r + 2][c] + graph[r + 2][c + 1],
            )
        #  ■
        #  □
        # □□
        if r >= 0 and r + 2 < n and c - 1 >= 0 and c < m:
            answer = max(
                answer,
                graph[r][c] + graph[r + 1][c] + graph[r + 2][c] + graph[r + 2][c - 1],
            )
        #   □
        # ■□□
        if r - 1 >= 0 and r < n and c >= 0 and c + 2 < m:
            answer = max(
                answer,
                graph[r][c] + graph[r][c + 1] + graph[r][c + 2] + graph[r - 1][c + 2],
            )
        # ■
        # □□□
        if r >= 0 and r + 1 < n and c >= 0 and c + 2 < m:
            answer = max(
                answer,
                graph[r][c]
                + graph[r + 1][c]
                + graph[r + 1][c + 1]
                + graph[r + 1][c + 2],
            )
        # ■□
        #  □
        #  □
        if r >= 0 and r + 2 < n and c >= 0 and c + 1 < m:
            answer = max(
                answer,
                graph[r][c]
                + graph[r][c + 1]
                + graph[r + 1][c + 1]
                + graph[r + 2][c + 1],
            )
        # ■□
        # □
        # □
        if r >= 0 and r + 2 < n and c >= 0 and c + 1 < m:
            answer = max(
                answer,
                graph[r][c] + graph[r][c + 1] + graph[r + 1][c] + graph[r + 2][c],
            )
        # ■□□
        # □
        if r >= 0 and r + 1 < n and c >= 0 and c + 2 < m:
            answer = max(
                answer,
                graph[r][c] + graph[r][c + 1] + graph[r][c + 2] + graph[r + 1][c],
            )
        # ■□□
        #   □
        if r >= 0 and r + 1 < n and c >= 0 and c + 2 < m:
            answer = max(
                answer,
                graph[r][c] + graph[r][c + 1] + graph[r][c + 2] + graph[r + 1][c + 2],
            )

print(answer)
