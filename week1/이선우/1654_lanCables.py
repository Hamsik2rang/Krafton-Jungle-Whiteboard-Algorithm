import sys

iter, total_cables = map(int, sys.stdin.readline().split())
original_list = []
for i in range(iter):
    original_list.append(int(sys.stdin.readline()))
start = 0
end = max(original_list)

def check(cable_length: int, goal: int):
    cable_output = 0

    for cable in original_list:
        cable_output += cable // cable_length
    if cable_output > goal:
        return 1
    elif cable_output < goal:
        return 2
    else:
        return 3



    



while True:
    mid = (start + end)//2
    case = check(mid, total_cables)

    if case == 1:
        start = mid
    elif case == 2:
        end = mid
    else:
        while case == 3:
            mid += 1
            case = check(mid, total_cables)
        mid -= 1
        print(mid)
        break


