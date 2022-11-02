import sys


def lotto(depth=6, s=0, arr=[]):
    if depth == 0:
        print(" ".join(list(map(str, arr))))
    else:
        for i in range(s, len(numbers) - (depth - 1)):
            lotto(depth - 1, i + 1, arr[:] + [numbers[i]])


line = False
while True:
    TC = list(map(int, sys.stdin.readline().split()))
    if TC[0] == 0:
        break
    if line:
        print("")
    else:
        line = True
    k = TC[0]
    numbers = TC[1:]
    lotto()
