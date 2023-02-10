# time out
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

# prefix sum
def solution(board, skill):
    # set value for prefix sum
    def cast(board, skill):
        height, width = len(board), len(board[0])
        type, r1, c1, r2, c2, degree = skill
        flag = -1 if type == 1 else 1
        # left top++
        board[r1][c1] += flag * degree
        # left bottom--
        if r2 + 1 < height:
            board[r2 + 1][c1] -= flag * degree
        # right top--
        if c2 + 1 < width:
            board[r1][c2 + 1] -= flag * degree
            # left bottom++
            if r2 + 1 < height:
                board[r2 + 1][c2 + 1] += flag * degree

    height, width = len(board), len(board[0])
    # newBoard for prefix sum
    newBoard = list([0] * width for _ in range(height))
    # set value for prefix sum on newBoard
    for i in skill:
        cast(newBoard, i)
    # prefix sum sidewards
    for row in range(height):
        for col in range(1, width):
            newBoard[row][col] += newBoard[row][col - 1]
    # prefix sum downwards
    for row in range(1, height):
        for col in range(width):
            newBoard[row][col] += newBoard[row - 1][col]
    # count destroyed
    answer = 0
    for row in range(height):
        for col in range(width):
            if board[row][col] + newBoard[row][col] > 0:
                answer += 1
    return answer