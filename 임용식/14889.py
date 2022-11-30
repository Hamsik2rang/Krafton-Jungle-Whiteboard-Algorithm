import sys


def calculate_score():
    global n
    team_a, team_b = [], []
    for i in range(n):
        if is_selected[i]:
            team_a.append(i)
        else:
            team_b.append(i)
    score_a = 0
    for i in range(len(team_a) - 1):
        for j in range(i + 1, len(team_a)):
            score_a += graph[team_a[i]][team_a[j]] + graph[team_a[j]][team_a[i]]
    score_b = 0
    for i in range(len(team_b) - 1):
        for j in range(i + 1, len(team_b)):
            score_b += graph[team_b[i]][team_b[j]] + graph[team_b[j]][team_b[i]]

    return abs(score_a - score_b)


def solution(index: int, count: int) -> None:
    global n, answer, is_selected

    if count == n // 2:
        cur_score = calculate_score()
        answer = cur_score if answer < 0 else min(answer, cur_score)
        return

    for i in range(index, n):
        is_selected[i] = True
        solution(i + 1, count + 1)
        is_selected[i] = False


n = int(sys.stdin.readline())
graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, sys.stdin.readline().split()))

answer = -1
is_selected = [False for _ in range(n)]
solution(0, 0)
print(answer)
