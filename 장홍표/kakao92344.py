def solution(board, skill):
    answer = 0

    for i in range(len(skill)):
        team, r1, c1, r2, c2, value = skill[i]
        for j in range(r1,r2+1):
            for k in range(c1,c2+1):
                if(team ==1):
                    board[j][k] -= value
                else:
                    board[j][k] += value
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(board[i][j]>0):
                answer += 1
    return answer
#시간초과

