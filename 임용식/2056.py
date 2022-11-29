import sys


class Node:
    def __init__(self):
        self.cost = 0
        self.before_list = []


def solution(node: int) -> None:
    check[node] = True

    for before_node in node_pool[node].before_list:
        if not check[before_node]:
            solution(before_node)
    max_before_cost = 0
    for before_node in node_pool[node].before_list:
        max_before_cost = max(max_before_cost, node_pool[before_node].cost)
    node_pool[node].cost += max_before_cost


n = int(sys.stdin.readline())
node_pool = [Node() for _ in range(10001)]
check = [False for _ in range(10001)]
in_degree = [0 for _ in range(10001)]
for i in range(1, n + 1):
    input_list = list(map(int, sys.stdin.readline().split()))
    node_pool[i].cost = input_list[0]
    for j in range(input_list[1]):
        node_pool[i].before_list.append(input_list[2 + j])
        in_degree[input_list[2 + j]] += 1

for i in range(1, n + 1):
    if in_degree[i] == 0:
        solution(i)

max_time = 0
for i in range(1, n + 1):
    max_time = max(max_time, node_pool[i].cost)
print(max_time)
