import sys

sys.stdin = open("input.txt", "r")


import sys


def DFS(s="", n=0):
    if n == L:
        arr.append(s)
    else:
        for alp in alps:
            if dct[alp]:
                dct[alp] -= 1
                DFS(s + alp, n + 1)
                dct[alp] += 1


N = int(sys.stdin.readline())
words = [sys.stdin.readline().rstrip() for _ in range(N)]
result = []
for word in words:
    L = len(word)
    dct = {chr(i): 0 for i in range(97, 123)}
    for c in word:
        dct[c] += 1
    alps = []
    for k, v in dct.items():
        if v:
            alps.append(k)
    arr = []
    DFS()
    result.extend(arr)
result = sorted(list(set(result)), key=lambda x: (len(x), x))
for one in result:
    print(one)
