import sys
import itertools
input = sys.stdin.readline

# itertools.combinations
while True:
    s = list(map(int, input().split()))
    # escape
    if s[0] == 0:
        break
    # pop or remove s[0]==k
    k = s.pop(0)
    cases = list(itertools.combinations(s, 6))
    for case in cases:
        for num in case:
            print(num, end=' ')
        print()
    print()

# rec
def comb(li, n):
    tab = []
    # escape
    if n == 0:
        return [[]]

    for i in range(len(li)):
        for rest in comb(li[i+1:], n-1):
            tab.append([li[i]] + rest)
    return tab

while True:
    s = list(map(int, input().split()))
    # escape
    if s[0] == 0:
        break
    # pop or remove s[0]==k
    k = s.pop(0)
    cases = comb(s, 6)
    for case in cases:
        for num in case:
            print(num, end=' ')
        print()
    print()
