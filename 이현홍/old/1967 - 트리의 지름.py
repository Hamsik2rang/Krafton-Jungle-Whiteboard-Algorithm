import sys

sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
mx = -1
edges = {i: [] for i in range(1, N + 1)}
weights = [0] * (N + 1)
for _ in range(N - 1):
    parent, child, weight = map(int, sys.stdin.readline().split())
    edges[parent].append(child)
    weights[child] = weight


def choice(node=1):
    if edges[node]:
        parts = sorted(tuple(map(lambda x: choice(x), edges[node])), reverse=True)
        if 2 <= len(edges[node]):
            global mx
            mx = sum(parts[:2]) if mx < sum(parts[:2]) else mx
        return weights[node] + parts[0]
    else:
        return weights[node]


n = choice()
print(max(mx, n))
