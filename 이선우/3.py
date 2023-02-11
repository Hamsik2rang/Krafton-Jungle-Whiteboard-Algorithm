def solution(board, skill):
    answer = 0
    for s in skill:
        type, r1, c1, r2, c2, degree = s[0], s[1], s[2], s[3], s[4], s[5]
        
        if (type == 1):
            for row in range(r1, r2 + 1):
                for col in range(c1, c2 + 1):
                    board[row][col] -= degree
        else:
            for row in range(r1, r2 + 1):
                for col in range(c1, c2 + 1):
                    board[row][col] += degree
        
    for buildings in board:
        for building in buildings:
            if building > 0:
                answer += 1
    return answer
