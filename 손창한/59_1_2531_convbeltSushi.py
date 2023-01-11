import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().rsplit())
a = [int(input().rstrip()) for _ in range(n)]
a += a[:k]
print(max[([len(set(a[i:i+k]) | set([c])) for i in range(n)]))
