import numpy as np

def solution(board, skill):
    answer = 0
    tmp = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    
    for type, r1, c1, r2, c2, degree in skill:
        tmp[r1][c1] += degree if type == 2 else -degree
        tmp[r1][c2 + 1] += -degree if type == 2 else degree
        tmp[r2 + 1][c1] += -degree if type == 2 else degree
        tmp[r2 + 1][c2 + 1] += degree if type == 2 else -degree
    
    for i in range(len(tmp) - 1):
        for j in range(len(tmp[0]) - 1):
            tmp[i][j + 1] += tmp[i][j]
    for j in range(len(tmp[0]) - 1):
        for i in range(len(tmp) - 1):
            tmp[i + 1][j] += tmp[i][j]
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] += tmp[i][j]
            # board에 값이 1이상인 경우 answer++
            if board[i][j] > 0: answer += 1

    return answer

#-----------효율성 실패------------
# def attack(info, board):
#     lt_y, lt_x, rb_y, rb_x, point=info
#     board[lt_y:rb_y+1,lt_x:rb_x+1]=board[lt_y:rb_y+1,lt_x:rb_x+1]-point
#     return board

# def heal(info, board):
#     lt_y, lt_x, rb_y, rb_x, point=info
#     board[lt_y:rb_y+1,lt_x:rb_x+1]=board[lt_y:rb_y+1,lt_x:rb_x+1]+point
#     return board

# def solution(board, skill):
#     board=np.array(board)
#     for turn in range(len(skill)):
#         t_type,t_info=skill[turn][0], skill[turn][1:]
#         if t_type==1:
#             board=attack(t_info, board)
#         if t_type==2:
#             board=heal(t_info, board)

#     return len(np.where(board>0)[0])
    
