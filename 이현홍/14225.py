import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()


arr = [1] * (2**20 + 1)
arr[0] = 0
arr[numbers[0]] = 0
for number in numbers[1:]:
    temps = [0]
    for i in range(2**20 + 1 - number):
        if not arr[i]:
            temps.append(i)
    for temp in temps:
        arr[temp + number] = 0


for idx in range(1, 2**20 + 1):
    if arr[idx]:
        print(idx)
        exit()
