import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def merge_sort(li, left, right):
    def merge(li, left, mid, right):
        # count swap
        global cnt
        tmp = 0
        # left[i], right[j]
        i, j = left, mid+1
        # buf[k]
        k = left
        # left, right >sort> buf
        while i <= mid and j <= right:
            if li[i] <= li[j]:
                buf[k] = li[i]
                i += 1
                # *** swap += idx_dif ***
                cnt += tmp
            else:
                buf[k] = li[j]
                j += 1
                # *** idx_dif++ ***
                tmp += 1
            k += 1
        # left done, copy right_rest
        if i > mid:
            for l in range(j, right+1):
                buf[k] = li[l]
                k += 1
        # right done, copy left_rest
        else:
            for l in range(i, mid+1):
                buf[k] = li[l]
                k += 1
                # *** swap += idx_dif ***
                cnt += tmp
        # buf >> li
        for p in range(left, right+1):
            li[p] = buf[p]

    if left < right:
        # devide
        mid = (left + right)//2
        # conquer
        merge_sort(li, left, mid)
        merge_sort(li, mid+1, right)
        # combine
        merge(li, left, mid, right)

n = int(input())
li = list(map(int, input().split()))

buf = [None] * n
cnt = 0
merge_sort(li, 0, n-1)

print(cnt)
