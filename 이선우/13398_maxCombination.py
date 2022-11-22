import sys

sys.stdin = open("input.txt", "r")

import sys

iter = int(sys.stdin.readline())
given_list = list(map(int, sys.stdin.readline().split()))
new_list = []

temp = 0
for num in given_list:
    if num >= 0:
        temp += num
    else:
        new_list.append(temp)
        new_list.append(num)
        temp = 0

result_list = []
longest_streak = 0

for num in range(0, len(new_list), 2):
    if num == len(new_list) - 1 or num == len(new_list) - 2:
        result_list.append(new_list[num])
    else:
        longest_streak += new_list[num] + new_list[num + 1]
    if longest_streak >= 0:
        continue
    else:
        result_list.append(longest_streak + abs(new_list[num + 1]))
        result_list.append(new_list[num + 1])
        longest_streak = 0

max = 0
for num in range(len(result_list), 2):
    if num == len(new_list) - 1 or num == len(new_list) - 2:
        temp = result_list[num]
    else:
        temp = result_list[num] + result_list[num + 2]
    if temp > max:
        max = temp

print(max)