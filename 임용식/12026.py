import sys

n = int(sys.stdin.readline())
string = sys.stdin.readline().strip()
b_index, o_index, j_index = [], [], []
for i in range(len(string)):
    if string[i] == "B":
        b_index.append(i)
    elif string[i] == "O":
        o_index.append(i)
    else:
        j_index.append(i)
memo = [0x7FFFFFFF for _ in range(n + 1)]

memo[0] = 0
for i in range(1, n):
    if string[i] == "B":
        for j in j_index:
            if j > i:
                break
            memo[i] = min(memo[i], (j - i) ** 2 + memo[j])
    elif string[i] == "O":
        for j in b_index:
            if j > i:
                break
            memo[i] = min(memo[i], (j - i) ** 2 + memo[j])
    elif string[i] == "J":
        for j in o_index:
            if j > i:
                break
            memo[i] = min(memo[i], (j - i) ** 2 + memo[j])

print(-1 if memo[n - 1] == 0x7FFFFFFF else memo[n - 1])
