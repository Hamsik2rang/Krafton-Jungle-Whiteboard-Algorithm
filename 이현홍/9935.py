import sys

string = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()
len_str = len(string)
len_bomb = len(bomb)

stack = []
for s in string:
    stack.append(s)
    if "".join(stack[-len_bomb:]) == bomb:
        for _ in range(len_bomb):
            stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")
