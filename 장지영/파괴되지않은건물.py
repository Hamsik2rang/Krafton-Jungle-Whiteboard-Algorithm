


def solution(board, skill):
    answer = 0
    
    for turn in skill : 
        isEnemy, r1, c1, r2, c2, degree = turn
        if isEnemy == 1 : # 적의 공격 
            for row in range(r1, r2 + 1) : 
                for col in range(c1, c2 + 1) : 
                    board[row][col] -= degree 
        else : # 아군 회복
            for row in range(r1, r2 + 1) : 
                for col in range(c1, c2 + 1) : 
                    board[row][col] += degree 
    
    for row in board : 
        for col in row : 
            if col > 0 : 
                answer += 1
    
    return answer
