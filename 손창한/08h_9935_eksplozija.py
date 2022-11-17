import sys
input = sys.stdin.readline

# implement stack
class stack:
    def __init__(self):
        self.stk = []
        self.pt = -1
    def push(self, x):
        self.stk.append(x)
        self.pt += 1
    def pop(self):
        if self.pt == -1:
            return -1
        tmp = self.stk[self.pt]
        del self.stk[self.pt]
        self.pt -= 1
        return tmp
    def size(self):
        return self.pt + 1
    def empty(self):
        return 1 if self.pt == -1 else 0
    def top(self):
        if self.pt == -1:
            return -1
        return self.stk[self.pt]
    def show(self):
        return self.stk

s = list(input().rstrip())
b = list(input().rstrip())

#stack = []
#for c in s:
#    stack.append(c)
#    if len(stack) >= len(b) and stack[-1] == b[-1]:
#        if stack[-len(b):] == b:
#            for _ in range(len(b)):
#                stack.pop()
#print("".join(stack) if stack else "FRULA")

stck = stack()
for c in s:
    stck.push(c)
    if stck.size() >= len(b) and stck.top() == b[-1]:
        temp = stack()
        for i in range(len(b)):
            if stck.top() == b[-(i+1)]:
                temp.push(stck.pop())
            else:
                for _ in range(temp.size()):
                    stck.push(temp.pop())
                break
print("".join(stck.show()) if stck.size() else "FRULA")
