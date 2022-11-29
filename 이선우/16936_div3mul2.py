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

if ans_list == []:
    for num in num_list:
        temp = math.log(num) / math.log(3)
        print(temp)
        if (temp - int(temp) == 0):
            print(1)
            pass
        else:
            print(2)
            ans_list.append(num)

if ans_list == []:
    num_list.sort(reverse=True)
    for num in num_list:
        print(num, end=' ')
    exit()

ans_list.sort()

# 이전 순서 값 찾기
while len(ans_list) != length:
    if ans_list[0] * 3 in num_list:
        ans_list.insert(0, ans_list[0] * 3)
    else:
        ans_list.insert(0, int(ans_list[0] / 2))

for num in ans_list:
    print(num, end=' ')