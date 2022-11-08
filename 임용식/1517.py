import sys

ans = 0


def merge_sort(lst: list, left: int, right: int) -> None:
    global ans
    if left == right:
        return

    mid = (left + right) // 2
    merge_sort(lst, left, mid)
    merge_sort(lst, mid + 1, right)

    temp = []

    lp, rp = left, mid + 1
    while lp <= mid and rp <= right:
        if lst[lp] <= lst[rp]:
            temp.append(lst[lp])
            lp += 1
        else:
            temp.append(lst[rp])
            ans += mid - lp + 1
            rp += 1

    while lp <= mid:
        temp.append(lst[lp])
        lp += 1
    while rp <= right:
        temp.append(lst[rp])
        rp += 1

    for i in range(len(temp)):
        lst[left + i] = temp[i]

    del temp


n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

merge_sort(lst, 0, n - 1)
print(ans)
