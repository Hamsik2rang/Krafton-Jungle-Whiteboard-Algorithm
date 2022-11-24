import sys


def is_promise() -> bool:
    global min_diff
    if selected_list[-1] - selected_list[0] < min_diff:
        return False

    difficulty_sum = sum(selected_list)
    if difficulty_sum < min_sum or difficulty_sum > max_sum:
        return False

    return True


def solution(index: int) -> None:
    global n, answer
    if len(selected_list) >= 2:
        if is_promise():
            answer += 1

        if len(selected_list) == len(problem_list):
            return

    for i in range(index, n):
        selected_list.append(problem_list[i])
        solution(i + 1)
        selected_list.pop()


n, min_sum, max_sum, min_diff = map(int, sys.stdin.readline().split())
answer = 0
problem_list = list(map(int, sys.stdin.readline().split()))
selected_list = []

problem_list.sort()
solution(0)

print(answer)
