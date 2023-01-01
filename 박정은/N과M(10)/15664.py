def combination(arr, n):
    result = []
    if n == 0:
        return [[]]

    for i in range(len(arr)):
        elem = arr[i]
        for rest in combination(arr[i + 1:], n - 1):
            result.append([elem] + rest)
    return result


n, m = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort()

check = combination(lst, m)
buff = []

for one in check:

    if one not in buff:
        buff.append(one)
        print(*one)
