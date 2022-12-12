import sys

sys.stdin = open("input.txt", "r")

import sys
from itertools import combinations

iter = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
sum_list = [0 for _ in range(100000 * iter)]
sum_list[0] = 1

for i in range(1, iter + 1):
    for number in combinations(num_list, i):
        sum_list[sum(number)] = 1


print(sum_list.index(0))