import sys

sys.stdin = open("input.txt", "r")

import sys
import math

length = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
ans_list = []

# 마지막 값 찾기
for num in num_list:
    if num % 3 != 0:
        ans_list.append(num)
# 마지막 값 찾기
if ans_list == []:
    temp = math.log(num) / math.log(3)
    if (temp - int(temp) == 0):
        pass
    else:
        ans_list.append(num)

ans_list.sort()

# 이전 순서 값 찾기
while len(ans_list) != length:
    if ans_list[0] * 3 in num_list:
        ans_list.insert(0, ans_list[0] * 3)
    else:
        ans_list.insert(0, int(ans_list[0] / 2))

for num in ans_list:
    print(num, end=' ')