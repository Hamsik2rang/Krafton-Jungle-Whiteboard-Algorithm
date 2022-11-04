import sys


def search(lecture_list: list, left: int, right: int, cnt: int) -> int:
    ans = 100_000_000
    while left <= right:
        mid = (left + right) // 2
        index = 0
        sum_list = []
        while index < len(lecture_list) and len(sum_list) < cnt:
            sum = 0
            while index < len(lecture_list) and sum + lecture_list[index] <= mid:
                sum += lecture_list[index]
                index += 1
            if sum == 0:
                break
            sum_list.append(sum)

        if index < len(lecture_list):
            left = mid + 1
        else:
            ans = min(ans, max(sum_list))
            right = mid - 1
    return ans


n, m = map(int, sys.stdin.readline().split())
lecture_list = list(map(int, sys.stdin.readline().split()))
ans = search(lecture_list, 1, 100_000_000, m)

print(ans)
