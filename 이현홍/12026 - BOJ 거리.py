import sys

N = int(sys.stdin.readline())
string = sys.stdin.readline().rstrip()
visit = [0xFFFFFFF] * N
visit[0] = 0
for i in range(N - 1):
    for j in range(i, N):
        if string[i] == "B" and string[j] == "O" and visit[i] + (j - i) ** 2 < visit[j]:
            visit[j] = visit[i] + (j - i) ** 2
        if string[i] == "O" and string[j] == "J" and visit[i] + (j - i) ** 2 < visit[j]:
            visit[j] = visit[i] + (j - i) ** 2
        if string[i] == "J" and string[j] == "B" and visit[i] + (j - i) ** 2 < visit[j]:
            visit[j] = visit[i] + (j - i) ** 2

print(-1) if visit[-1] == 0xFFFFFFF else print(visit[-1])
