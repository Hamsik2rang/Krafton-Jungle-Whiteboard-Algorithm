import sys

N = int(sys.stdin.readline())

s = 1

Q = [0] * 1000000
visit = [[1 for _ in range(2001)] for __ in range(1020)]
visit[0][0] = 0
front = -1
rear = -1

rear += 1
Q[rear] = (0, 1, 0)

while True:
    front += 1
    clipboard, now, idx = Q[front]
    if now and now < 1002:
        if clipboard:
            if now + clipboard <= 2000 and visit[clipboard][now]:
                rear += 1
                visit[clipboard][now] = 0
                Q[rear] = (clipboard, now + clipboard, idx + 1)
                if now + clipboard == N:
                    print(idx + 1)
                    break
        if visit[clipboard][now - 1]:
            visit[clipboard][now - 1] = 0
            rear += 1
            Q[rear] = (clipboard, now - 1, idx + 1)
            if now - 1 == N:
                print(idx + 1)
                break
        if clipboard != now:
            rear += 1
            Q[rear] = (now, now, idx + 1)
            if now + clipboard == N:
                print(idx + 1)
                break
