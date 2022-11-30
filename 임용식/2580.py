import sys


def get_nr_and_nc(row: int, col: int) -> tuple:
    nr = row
    nc = col + 1
    if nc == 9:
        nr += 1
        nc %= 9
    return (nr, nc)


def is_promise(row: int, col: int, num: int) -> bool:
    # 3*3 사각형 안의 유망성 판단
    row_start = row // 3 * 3
    col_start = col // 3 * 3
    row_end = row_start + 3
    col_end = col_start + 3
    for cr in range(row_start, row_end):
        for cc in range(col_start, col_end):
            cur = board[cr][cc]
            if cur == num:
                return False

    # 행의 유망성 판단
    for cr in range(9):
        if cr == row:
            continue
        if board[cr][col] == num:
            return False

    # 열의 유망성 판단
    for cc in range(9):
        if cc == col:
            continue
        if board[row][cc] == num:
            return False

    return True


def solution(count: int) -> None:
    if count == len(zero):
        for _ in range(9):
            print(*board[_])
        exit(0)

    for num in range(1, 10):
        row = zero[count][0]
        col = zero[count][1]

        if is_promise(row, col, num):
            board[row][col] = num
            solution(count + 1)
            board[row][col] = 0


board = [[0 for i in range(9)] for j in range(9)]
zero = []


for i in range(9):
    board[i] = list(map(int, sys.stdin.readline().split()))
    for j in range(9):
        if board[i][j] == 0:
            zero.append((i, j))


solution(0)
