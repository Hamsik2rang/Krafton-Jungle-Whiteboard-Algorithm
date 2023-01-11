import sys

sys.stdin = open("input.txt", "r")


# 메모리 102360KB 시간 332ms
import sys

K, L = map(int, sys.stdin.readline().split())
check = set()
aligned = []

applier = tuple(map(lambda x: x.strip(), sys.stdin.readlines()))
for idx in range(-1, -L - 1, -1):
    if not applier[idx] in check:
        check.add(applier[idx])
        aligned.append(applier[idx])

print("\n".join(aligned[-1 : -K - 1 : -1]))

# 메모리 	102352KB 시간 392ms
import sys

K, L = map(int, sys.stdin.readline().split())
dct = {}
appliers = tuple(map(lambda x: x.strip(), sys.stdin.readlines()))
priority = 0
for applier in appliers:
    priority += 1
    dct[applier] = priority

print("\n".join(sorted(dct.keys(), key=lambda x: dct[x])[:K]))

# 메모리 60616KB 시간 328ms
import sys

K, L = map(int, sys.stdin.readline().split())
dct = {sys.stdin.readline().strip(): i for i in range(L)}
print("\n".join(sorted(dct.keys(), key=lambda x: dct[x])[:K]))
