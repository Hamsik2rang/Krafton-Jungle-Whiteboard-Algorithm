import sys

ans = []


def get_skip(txt: str, pat: str) -> list:
    skip = [0] * len(pat)
    j = 0
    for i in range(1, len(pat)):
        while j > 0 and pat[i] != pat[j]:
            j = skip[j - 1]
        if pat[i] == pat[j]:
            j += 1
            skip[i] = j
    return skip


def kmp(txt: str, pat: str) -> int:
    skip = get_skip(txt, pat)

    i = j = 0
    while i != len(txt) and j != len(pat):
        if txt[i] == pat[j]:
            i += 1
            j += 1
        elif j == 0:
            i += 1
        else:
            j = skip[j - 1]

        if j == len(pat):
            ans.append(i - j + 1)
            j = skip[j - 1]


s1 = input()
s2 = input()
idx = kmp(s1, s2)
print(len(ans))
for i in ans:
    print(i)
