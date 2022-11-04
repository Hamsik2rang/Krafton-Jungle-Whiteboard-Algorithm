import sys

sys.setrecursionlimit(10**5)

ans = 0


def str_to_bitset(s: str) -> int:
    lst = list(set(s))
    bitset = 0
    for c in lst:
        bitset |= 1 << (ord(c) - ord("a"))
    return bitset


def solution(bitset: int, index: int, cnt: int, k: int) -> None:
    global ans
    if cnt == k:
        readable = 0
        for word in bitset_list:
            if word & bitset == word:
                readable += 1
        ans = max(ans, readable)
        return

    for i in range(index, 26):
        if bitset & (1 << i) == (1 << i):
            continue
        origin = bitset
        bitset |= 1 << i
        solution(bitset, i + 1, cnt + 1, k)
        bitset = origin


n, k = map(int, sys.stdin.readline().split())
if k < 5:
    print(0)
    exit(0)

bitset_list = []
for i in range(n):
    s = sys.stdin.readline().strip()
    bitset_list.append(str_to_bitset(s))

knowledge = str_to_bitset("antatica")
solution(knowledge, 0, 5, k)
print(ans)
