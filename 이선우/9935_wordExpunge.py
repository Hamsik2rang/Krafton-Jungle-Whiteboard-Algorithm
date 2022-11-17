import sys

sys.stdin = open("input.txt", "r")

import sys

input_str = str(sys.stdin.readline())
bomb = str(sys.stdin.readline())
ans = []
counter = 0

for char in input_str:
    ans.append(char)
    if char == bomb[-1] and ''.join(ans[-len(bomb):]) == bomb:
        del ans[-len(bomb):]

ans = ''.join(ans)
if ans:
    print(ans)
else:
    print('FRULA')