def solution(board, skill):
    for type, r1, c1, r2, c2, degree in skill:
        flag = -1 if type == 1 else 1
        for row in range(r1, r2+1):
            for col in range(c1, c2+1):
                board[row][col] += flag * degree

    answer = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] > 0:
                answer += 1

    return answer
