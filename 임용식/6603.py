import sys
import itertools

while True:
    lst = list(map(int, sys.stdin.readline().split()))

    cnt = lst[0]
    if cnt == 0:
        break
    lst = lst[1:]
    for comb in itertools.combinations(lst, 6):
        print(*comb)
    print()
