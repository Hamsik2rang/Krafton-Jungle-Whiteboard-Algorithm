import sys


def is_exploded(stk: list, explosion: str) -> bool:
    return "".join(stk[len(stk) - len(explosion) :]) == explosion


string = sys.stdin.readline().strip()
explosion = sys.stdin.readline().strip()

stk = []

for c in string:
    stk.append(c)

    if is_exploded(stk, explosion):
        for _ in range(len(explosion)):
            stk.pop()

if len(stk) == 0:
    print("FRULA")
else:
    print("".join(stk))
