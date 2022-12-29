# import sys

# sys.stdin = open("input.txt", "r")

# import sys

# iter = int(sys.stdin.readline())

# def stonks(stonk):
#     temp_list = []
#     global profit

#     if len(stonk) <= 1:
#         print(profit)
#         return

#     for num in range(len(stonk)):
#         if stonk[num] < max(stonk):
#             temp_list.append(stonk[num])
#         elif stonk[num] == max(stonk):
#             profit += max(stonk) * len(temp_list) - sum(temp_list)
#             stonks(stonk[stonk.index(stonk[num]) + 1:])
#             break

# for _ in range(iter):
#     count = int(sys.stdin.readline())
#     num_list = list(map(int, sys.stdin.readline().split()))
#     profit = 0

#     stonks(num_list)

import sys

iter = int(sys.stdin.readline())

def stonks(stonk):
    profit = 0
    temp_max = stonk[0]

    for num in range(1, len(stonk)):
        if stonk[num] <= temp_max:
            profit += temp_max - stonk[num]
        elif stonk[num] > temp_max:
            temp_max = stonk[num]
    print(profit)

for _ in range(iter):
    count = int(sys.stdin.readline())
    num_list = list(map(int, sys.stdin.readline().split()))
    num_list.reverse()

    stonks(num_list)