import sys
input = sys.stdin.readline

def bt(x):
    global e
    # escape
    if len(w) == 2:
        e = max(e, x)
        return
    for i in range(1, len(w)-1):
        m = w[i-1] * w[i+1]
        tmp = w.pop(i)
        bt(x+m)
        w.insert(i, tmp)

n = int(input())
w = list(map(int, input().split()))
e = 0
bt(0)
print(e)
