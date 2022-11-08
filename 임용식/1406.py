import sys

left_stk, right_stk = [], []

string = sys.stdin.readline().strip()
n = int(sys.stdin.readline())
for c in string:
    left_stk.append(c)

while n > 0:
    n -= 1

    cmd = sys.stdin.readline().strip().split()
    if cmd[0] == "P":
        num = cmd[1]
        left_stk.append(num)
    elif cmd[0] == "L":
        if len(left_stk) > 0:
            right_stk.append(left_stk.pop())
    elif cmd[0] == "D":
        if len(right_stk) > 0:
            left_stk.append(right_stk.pop())
    else:
        if len(left_stk) > 0:
            left_stk.pop()

for c in left_stk:
    print(c, end="")
right_stk.reverse()
for c in right_stk:
    print(c, end="")
