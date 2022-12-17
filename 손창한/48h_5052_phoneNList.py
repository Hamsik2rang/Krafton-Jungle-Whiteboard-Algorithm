import sys
input = sys.stdin.readline

# trie: tree for str
class Node():
    def __init__(self, key, data=None):
        self.key = key
        self.data = data # or fin_flg
        self.chld = {} # python ? dict : list

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        cur = self.head
        for char in string:
            if char not in cur.chld: # not exist: make new
                cur.chld[char] = Node(char)
            cur = cur.chld[char]
        cur.data = string

    def search(self, string):
        cur = self.head
        for char in stirng:
            if char in cur.chld:
                cur = cur.chld[char]
            else:
                return False
        # check data(str fin)
        if cur.data:
            return True
        else:
            return False

    def search_prf(self, string):
        cur = self.head
        for char in string:
            cur = cur.chld[char]
        # check fin
        if cur.chld:
            return False
        else:
            return True

t = int(input())
for _ in range(t):
    n = int(input())
    # init tree, search list
    trie = Trie()
    pl = []
    for _ in range(n):
        p = input().rstrip()
        pl.append(p)
        trie.insert(p)
    pl.sort()
    # for cases
    flg = True
    for p in pl:
        # if consistency: flg = False
        if not trie.search_prf(p):
            flg = False
    if flg:
        print("YES")
    else:
        print("NO")

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     pl = sorted(list(input().rstrip() for _ in range(n)))
#     flg = True
#     for i in range(n-1):
#         # sorted pl: comp bfr, nxt
#         if pl[i] == pl[i+1][:len(pl[i])]:
#             flg = False
#             break
#     if flg:
#         print("YES")
#     else:
#         print("NO")
