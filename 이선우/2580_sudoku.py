import sys

sys.stdin = open("input.txt", "r")

import sys

def check(coordinate, graph):
    cset = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    y_diff = list(set(cset) - set(graph[coordinate[0]]))
    if len(y_diff) == 1:
        return y_diff[0]
        
    x_diff = list(set(cset) - set([row[coordinate[1]] for row in graph]))
    if len(x_diff) == 1:
        return x_diff[0]
    
    box_xy = [(coordinate[0]// 3) * 3, (coordinate[1]// 3) * 3]
    box_set = []

    for temp in [[graph[y][x] for x in range(box_xy[1], box_xy[1] + 3)] for y in range(box_xy[0], box_xy[0] + 3)]:
        box_set.extend(temp)

    box_diff = list(set(cset) - set(box_set))
    
        

graph = []
missing_list = []

for i in range(9):
    tmp = list(map(int,input().split()))
    graph.append(tmp)

for y in range(0, 9):
    for x in range(0, 9):
        if graph[y][x] == 0:
            missing_list.append([y, x])
    
for missing_box in missing_list:
