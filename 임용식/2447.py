def star(row: int, col: int, n: int) -> None:
    if row // n % 3 == 1 and col // n % 3 == 1:
        print(" ", end="")
    else:
        if n == 1:
            print("*", end="")
        else:
            star(row, col, n // 3)


n = int(input())
for row in range(n):
    for col in range(n):
        star(row, col, n)
    print()
