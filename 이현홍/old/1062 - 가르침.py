import sys


def Antartica(count, idx, limit: int, alps: set):
    if idx == N:
        if limit < 0:
            return count - 1
        else:
            return count
    else:
        if limit < 0:
            return 0
        else:
            n = len(alps.union(words[idx]) - alps)
            return max(Antartica(count, idx + 1, limit, alps), Antartica(count + 1, idx + 1, limit - n, alps.union(words[idx])))


N, K = map(int, sys.stdin.readline().split())
counts = 0

if K < 5:
    print(0)
elif K == 26:
    print(N)
else:
    words = [set((" ".join(sys.stdin.readline().rstrip())).split()) - set(["a", "n", "t", "i", "c"]) for _ in range(N)]
    print(Antartica(0, 0, K - 5, set()))