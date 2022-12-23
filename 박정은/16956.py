def findWolf():
    drow = [0, 0, -1, 1]
    dcol = [-1, 1, 0, 0]
    for row in range(R):
        for col in range(C):

            if mokjang[row][col] == 'W':
                for i in range(4):
                    nrow = row + drow[i]
                    ncol = col + dcol[i]

                    if -1 < ncol < C and -1 < nrow < R:
                        if mokjang[nrow][ncol] == 'S':
                            return False
                        elif mokjang[nrow][ncol] == '.':
                            mokjang[nrow][ncol] = 'D'
    return True


R, C = map(int, input().split())

mokjang = []


for _ in range(R):
    mokjang.append(list(map(str, input())))

if findWolf():
    print(1)
    for one in mokjang:
        print(''.join(one))
else:
    print(0)
