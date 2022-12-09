N = int(input())

lst = " "+input().strip()
INF = 10e9

visited = [INF] * (N + 1)
visited[1] = 0


for i in range(1,N):
    for j in range(i+1,N+1):
        
        comp = visited[i]+(j-i)**2

        if lst[i] == 'B':
            if lst[j] == 'O' and visited[j] > comp:
                visited[j] = comp

        elif lst[i] == 'O':
            if lst[j] == 'J' and visited[j] > comp:
                visited[j] = comp

        elif lst[i] == 'J':
            if lst[j] == 'B' and visited[j] > comp:
                visited[j] = comp

if visited[-1] == INF :
    print(-1)
else:
    print(visited[-1])

