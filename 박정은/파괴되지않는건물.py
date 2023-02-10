def solution(board, skill):
    answer = 0
    
    for sk in skill:
        if sk[0] == 1:
            point = -sk[5]
        else: 
            point = sk[5]
        
        for i in range(sk[1],sk[3]+1):
            for j in range(sk[2],sk[4]+1):
                board[i][j] += point
    
    for elem in board:
        for x in elem:
            if x > 0:
                answer += 1
    return answer
