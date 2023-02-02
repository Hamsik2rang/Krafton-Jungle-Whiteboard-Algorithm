import sys
input = sys.stdin.readline

## stack
#s = input().rstrip()
#m = int(input())
#l_stk, r_stk = [], []
#l_stk.extend(s)
#
#for _ in range(m):
#    cmd = input().split()
#    fn = cmd[0]
#    # levo
#    if fn == "L":
#        if l_stk:
#            r_stk.append(l_stk.pop())
#    # dextro
#    elif fn == "D":
#        if r_stk:
#            l_stk.append(r_stk.pop())
#    # backspace
#    elif fn == "B":
#        if l_stk:
#            l_stk.pop()
#    # put
#    else:
#        l_stk.append(cmd[1])
#
#print(''.join(l_stk) + ''.join(r_stk[::-1])

# doubly linked list
class node():
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
# input
s = input().rstrip()
m = int(input())
# set linked list
cur = node(None)
for c in s:
    tmp = node(c)
    cur.next = tmp
    tmp.prev = cur
    cur = tmp
# cmd
for _ in range(m):
    cmd = input().split()
    fn = cmd[0]
    # levo
    if fn == "L":
        if cur.prev:
            cur = cur.prev
    # dextro
    elif fn == "D":
        if cur.next:
            cur = cur.next
    # backspace
    elif fn == "B":
        tmp = cur
        left = cur.prev
        right = cur.next
        if cur.data:
            left.next = right
            if right:
                right.prev = left
            cur = left
    # put
    else:
        tmp = node(cmd[1])
        right = cur.next
        if right:
            tmp.next = right
            right.prev = tmp
        cur.next = tmp
        tmp.prev = cur
        cur = tmp
# move cursor to start
while cur.data:
    cur = cur.prev
# print
while cur:
    if cur.data:
        print(cur.data, end="")
    cur = cur.next
