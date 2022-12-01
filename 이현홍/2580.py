import sys

sudoku = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
rows = [[1] * 10 for _ in range(9)]
cols = [[1] * 10 for _ in range(9)]
boxes = [[1] * 10 for _ in range(9)]

zeros = []
for r in range(9):
    for c in range(9):
        n = sudoku[r][c]
        if n:
            rows[r][n] = 0
            cols[c][n] = 0
            b = 3 * (r // 3) + (c // 3)
            boxes[b][n] = 0
        else:
            zeros.append((r, c))


def DFS(n=0):
    if n == len(zeros):
        for one in sudoku:
            print(" ".join(map(str, one)))
        exit()
    else:
        r, c = zeros[n]
        for temp in range(1, 10):
            if rows[r][temp] == cols[c][temp] == boxes[3 * (r // 3) + (c // 3)][temp] == 1:
                rows[r][temp], cols[c][temp], boxes[3 * (r // 3) + (c // 3)][temp] = 0, 0, 0
                sudoku[r][c] = temp
                DFS(n + 1)
                rows[r][temp], cols[c][temp], boxes[3 * (r // 3) + (c // 3)][temp] = 1, 1, 1
                sudoku[r][c] = 0


DFS()
