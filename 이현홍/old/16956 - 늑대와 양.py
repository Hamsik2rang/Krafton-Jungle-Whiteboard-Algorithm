import sys

R, C = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().strip()) for _ in range(R)]

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
for r in range(R):
    for c in range(C):
        if arr[r][c] == "W":
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < R and 0 <= nc < C:
                    if arr[nr][nc] == "S":
                        print(0)
                        exit()
                    elif arr[nr][nc] == ".":
                        arr[nr][nc] = "D"

print(1)
for r in range(R):
    print("".join(arr[r]))
