import sys
input = sys.stdin.readline

def dfs(idx, d):
    global ans
    # leaf(k - 5(acint))
    if d+5 == k:
        cnt = 0
        for w in li:
            for c in w:
                if not alpha[ord(c) - ord('a')]:
                    break
            else:
                cnt += 1
        ans = max(ans, cnt)
        return
    # search
    for i in range(idx, 26):
        if not alpha[i]:
            alpha[i] = True
            dfs(i, d+1)
            alpha[i] = False

n, k = map(int, input().split())
li = [set(input().rstrip()[4:-4]) for _ in range(n)]
ans = 0

# necessary = 5(acint)
if k < 5:
    print(0)
    exit(0)
# learned all alphabet
if k == 26:
    print(n)
    exit(0)
# alphabet list_boolean
alpha = [False] * 26
for c in "acint":
    alpha[ord(c)-ord('a')] = True

dfs(0, 0)
print(ans)
