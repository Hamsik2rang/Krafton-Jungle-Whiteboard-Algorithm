import sys
from collections import deque
input = sys.stdin.readline

# list
s = list(input().rstrip())
b = list(input().rstrip())
stack = []

for c in s:
    stack.append(c)
    if len(stack) >= len(b):
        if stack[-len(b)::] == b:
            for _ in range(len(b)):
                stack.pop()
print("".join(stack) if stack else "FRULA")
