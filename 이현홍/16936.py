import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))


def count(number):
    three = 0
    two = 0
    while not number % 3:
        number //= 3
        three -= 1
    while not number % 2:
        number //= 2
        two += 1
    return three, two


print(" ".join(map(str, sorted(arr, key=lambda x: count(x)))))
