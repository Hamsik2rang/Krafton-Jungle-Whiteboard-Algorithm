import sys


def comb(N, M):
    result = 1
    for n in range(N, N - M, -1):
        result *= n
    for m in range(M, 0, -1):
        result //= m
    return result


S, d, k, h = map(int, sys.stdin.readline().split())

if d + k + h < S:
    print(0)
    exit()

d, k, h = sorted([d, k, h])
result = 0
select_h = comb(S, h) % 1000000007
residue = S - h
for nk in range(k + 1):
    for nd in range(d, -1, -1):
        if residue == nk + nd:
            result += select_h * comb(residue, nk) * comb(S - nk, k - nk) * comb(h, d - nd)
            result %= 1000000007

print(result)
