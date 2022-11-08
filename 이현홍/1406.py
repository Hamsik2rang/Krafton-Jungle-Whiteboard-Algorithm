# 양방향 이동 접근법 고민해보기

import sys

string_left = " ".join(sys.stdin.readline().strip()).split()
M = int(sys.stdin.readline())

string_right = []
for _ in range(M):
    ipt = sys.stdin.readline().strip()
    if ipt == "L":
        if string_left:
            string_right.append(string_left.pop())
    elif ipt == "D":
        if string_right:
            string_left.append(string_right.pop())
    elif ipt == "B":
        if string_left:
            string_left.pop()
    else:
        ipt, s = ipt.split()
        string_left.append(s)

print("".join(string_left) + "".join(string_right[::-1]))
