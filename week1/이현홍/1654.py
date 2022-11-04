import sys

K, N = map(int, sys.stdin.readline().split())
arr = [int(n) for n in sys.stdin.readlines()]


def Promise(array, length, needs):
    craft = 0
    for one in array:
        craft += one // length
    if needs <= craft:
        return True
    return False


s = min(arr) // N
e = sum(arr) // N
while s <= e:
    length = (s + e) // 2
    cert = Promise(arr, length, N) if length else True
    if cert:
        s = length + 1
    else:
        e = length - 1
print((s + e) // 2)
