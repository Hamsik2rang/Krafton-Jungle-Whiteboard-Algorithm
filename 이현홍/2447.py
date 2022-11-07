import sys


def samsung(num):
    if num == 1:
        return ["***", "* *", "***"]
    else:
        prev = samsung(num - 1)
        result = []
        for turn in range(3):
            for p in prev:
                if turn == 1:
                    result.append(p + " " * (3 ** (num - 1)) + p)
                else:
                    result.append(p * 3)
        return result


N = int(sys.stdin.readline())
k = 0
while 3 <= N:
    k += 1
    N = N // 3
result = samsung(k)
for r in result:
    print(r)
