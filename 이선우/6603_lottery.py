import sys

trigger = True
while trigger:
    iter = list(map(int, sys.stdin.readline().split()))

    if iter[0] == 0:
        break
    else:
        num_count = iter[0]
        comb_nums = []
        for i in iter[1:]:
            comb_nums.append(i)
    


