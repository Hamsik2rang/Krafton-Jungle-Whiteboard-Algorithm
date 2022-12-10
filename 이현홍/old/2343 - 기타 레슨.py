import sys

N, M = map(int, sys.stdin.readline().split())
minutes = list(map(int, sys.stdin.readline().split()))


def counter(arr, limit):
    count = 1
    tmp_sum = 0
    for one in arr:
        if limit < one:
            return 0xFFFFFF
        else:
            if tmp_sum + one <= limit:
                tmp_sum += one
            else:
                count += 1
                tmp_sum = one
    return count


limit = max(sum(minutes) // M, max(minutes))

while True:
    while M < counter(minutes, limit):
        limit += 1
    while counter(minutes, limit - 1) <= M:
        limit -= 1
    print(limit)
    break
