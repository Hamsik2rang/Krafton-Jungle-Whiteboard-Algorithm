import sys

sys.setrecursionlimit(10**5)
# sys.stdin = open("input.txt", "r")

ans = 0


def solution(index: int, cnt: int, k: int) -> None:
    global ans
    if cnt == k:
        readable_count = 0
        for word in word_list:
            is_readable = True
            for c in word:
                if not readable_list[ord(c) - ord("a")]:
                    is_readable = False
                    break
            if is_readable:
                readable_count += 1
        ans = max(ans, readable_count)

    for i in range(index, 26):
        if not readable_list[i]:
            readable_list[i] = True
            solution(i + 1, cnt + 1, k)
            readable_list[i] = False


def set_readable(s: str) -> int:
    lst = list(set(s))
    for c in lst:
        readable_list[ord(c) - ord("a")] = True


n, k = map(int, sys.stdin.readline().split())
if k < 5:
    print(0)
    exit(0)

word_list = []
for i in range(n):
    s = sys.stdin.readline().strip()
    word_list.append(s)

readable_list = [False] * 26
set_readable("antatica")

solution(0, 5, k)
print(ans)
