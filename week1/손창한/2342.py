import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = list(map(int, input().split()))
# binary search
# left = maximum lesson >> bluray cap
left = max(li)
# right = sum of lessons
right = sum(li)

while left <= right:
    # mid = temp bluray
    mid = (left + right)//2
    # cnt = num of bluray, at least 1
    cnt = 1
    # tmp = temp sum of lessons
    tmp = 0

    for l in li:
        if tmp + l > mid:
            cnt += 1
            tmp = l
        else:
            tmp += l
    # bluray cap-- >> cnt++
    if cnt <= m:
        right = mid - 1
    # num of bluray over m >> bluray cap++ >> cnt--
    else:
        left = mid + 1
# left_fin = num of blurays
print(left)
