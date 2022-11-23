import sys

sys.stdin = open("input.txt", "r")

import sys

iter = int(sys.stdin.readline())
origami_list = []

def longest_subsequence(origami_list: list, size:int):
    length_list = [1] * size
    for num in range(1, size):
        temp_length = 0
        for i in range(0, num):
            if origami_list[i][1] <= origami_list[num][1]:
                temp_length = max(length_list[i], temp_length)
        length_list[num] = temp_length + 1
    print(max(length_list))

for _ in range(iter):
    a, b = map(int, sys.stdin.readline().split())
    origami_list.append([max(a, b), min(a, b)])

origami_list.sort()

longest_subsequence(origami_list, len(origami_list))