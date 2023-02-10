def solution(board, skill):
    for t, r1, c1, r2, c2, d in skill:
        t = -1 if t ==1 else 1
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                board[r][c] += t*d
    answer = 0
    for lst in board:
        for n in lst:
            if 0 < n:
                answer += 1
    return answer
