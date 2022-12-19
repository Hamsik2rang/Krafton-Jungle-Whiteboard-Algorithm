#n : the number of dots (ranges:3~500,000)
#m : the number of tries (ranges:3~1,000,000)

import sys
n, m = map(int, sys.stdin.readline().strip().split())
sys.setrecursionlimit(10**6)

# Define ROOT NODE list. Initially, each node are the root node of itself.
root_nodes = [i for i in range(500_000)]
answer = 1_000_001

# Define 'finding parent node' function
# Return : parent node index 
def find(node : int):
    if root_nodes[node] == node:
        return node
    else:
        parent = find(root_nodes[node])
        root_nodes[node] = parent
        return parent

# Define 'Uniting two disjoint set' function
# Return : True if parent of each disjoint set are same; False if parents are not same.
# If node1 parent and node2 parent are different, then unite two disjoint sets.
def union_find(node1 : int, node2 : int):
    node1 = find(node1)
    node2 = find(node2)
    
    if node1 == node2:
        return True
    else:
        if node1 < node2:
            root_nodes[node1] = node2
            return False
        else:
            root_nodes[node2] = node1
            return False

for j in range(m):
    node1, node2 = map(int, sys.stdin.readline().strip().split())
    if union_find(node1, node2):
        answer = min(answer, j+1)

if answer!=1_000_001:
    print (answer)
else:
    print (0)
