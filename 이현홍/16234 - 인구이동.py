import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

operators = dict(zip(["+", "-", "*", "//"], list(map(int, sys.stdin.readline().split()))))

mn = 10**9 + 1
mx = -(10**9 + 1)


def DFS(idx, s):
    if idx == N:
        global mn, mx
        if s < mn:
            mn = s
        if mx < s:
            mx = s
    else:
        for operator in operators.keys():
            if operators[operator]:
                operators[operator] -= 1
                if operator == "+":
                    DFS(idx + 1, s + arr[idx])
                if operator == "-":
                    DFS(idx + 1, s - arr[idx])
                if operator == "*":
                    DFS(idx + 1, s * arr[idx])
                if operator == "//":
                    if s < 0:
                        DFS(idx + 1, -(-s // arr[idx]))
                    else:
                        DFS(idx + 1, s // arr[idx])
                operators[operator] += 1


DFS(1, arr[0])
print(f"{mx}\n{mn}")
