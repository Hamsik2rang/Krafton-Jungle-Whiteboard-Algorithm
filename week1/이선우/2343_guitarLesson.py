import sys

lesson_count, bluray_count = map(int, sys.stdin.readline().split())
lesson_list = list(map(int, sys.stdin.readline().split()))
start = max(lesson_list)
end = sum(lesson_list)

def check(bluray_length: int, original_list: list):
    global bluray_count
    bluray_list = original_list
    temp_length = 0
    cycle = 1
    for lesson_no in range(0, len(bluray_list)):
        temp_length += bluray_list[lesson_no]
        if bluray_length == temp_length:
            if cycle < bluray_count:
                temp_length = 0
                cycle += 1
            else:
                return True
        elif bluray_length < temp_length:
            if cycle < bluray_count:
                temp_length = bluray_list[lesson_no]
                cycle += 1
            else:
                return True
    return False
                
while start <= end:
    mid = (start + end) // 2

    if check(mid, lesson_list):
        start = mid + 1
    else:
        end = mid - 1

print(start)