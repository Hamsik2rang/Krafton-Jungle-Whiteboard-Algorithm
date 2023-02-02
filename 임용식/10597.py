import sys


def dfs(index, arr):
    global max_element
    if index == len(s):
        print(*arr)
        exit()

    num1 = int(s[index])
    if not check[num1]:
        check[num1] = True
        arr.append(num1)
        dfs(index + 1, arr)
        check[num1] = False
        arr.pop()

    if index + 1 < len(s):
        num2 = int(s[index : index + 2])
        if num2 <= max_element and not check[num2]:
            check[num2] = True
            arr.append(num2)
            dfs(index + 2, arr)
            check[num2] = False
            arr.pop()


s = input()
max_element = len(s) if len(s) < 10 else 9 + (len(s) - 9) // 2
check = [0 for _ in range(max_element + 1)]

dfs(0, [])
