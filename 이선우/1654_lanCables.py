import sys

iter, total_cables = map(int, sys.stdin.readline().split())
original_list = [int(sys.stdin.readline()) for _ in range(iter)]
min_value = 1
max_value = max(original_list)

def check(cable_length: int, goal: int):
    cable_output = 0

    for cable in original_list:
        cable_output += cable // cable_length
    if cable_output >= goal:
        return True
    else:
        return False

while min_value <= max_value:
    mid = (min_value + max_value) // 2

    if check(mid, total_cables):
        min_value = mid + 1
    else:
        max_value = mid - 1

print(max_value)