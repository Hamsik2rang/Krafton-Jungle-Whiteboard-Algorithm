import sys

R, C = map(int, sys.stdin.readline().split())
arr = [[0] * C for _ in range(R)]
visit = [[0] * C for _ in range(R)]

for row in range(R):
    string = sys.stdin.readline().rstrip()
    for col in range(C):
        arr[row][col] = 0 if string[col] == "." else 1

cross = []

dir_r = [0, 1, 0, -1]
dir_c = [1, 0, -1, 0]
for row in range(1, R - 1):
    for col in range(1, C - 1):
        mx_len = min(row, col, R - row - 1, C - col - 1)
        if arr[row][col]:
            for l in range(1, mx_len + 1):
                check = True
                for k in range(4):
                    nr = row + dir_r[k] * l
                    nc = col + dir_c[k] * l
                    if not arr[nr][nc]:
                        check = False
                        break
                if check:
                    for k in range(4):
                        nr = row + dir_r[k] * l
                        nc = col + dir_c[k] * l
                        visit[nr][nc] = 1
                    visit[row][col] = 1
                    cross.append((row + 1, col + 1, l))
                else:
                    break

for row in range(R):
    for col in range(C):
        if arr[row][col] and not visit[row][col]:
            print(-1)
            exit()


print(len(cross))
for one in cross:
    print(one[0], one[1], one[2])
