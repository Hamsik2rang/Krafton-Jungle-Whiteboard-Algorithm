T = int(input())

for _ in range(T):
    
    N = int(input())
    lst = list(map(int, input().split()))

    big = 0
    ssum = 0

    for i in range(N-1, -1, -1):

        if lst[i] > big:
            big = lst[i]
        else:
            ssum += big-lst[i]

    print(ssum)
