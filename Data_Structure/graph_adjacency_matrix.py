# https://www.shafaetsplanet.com/planetcoding/?p=184

# 3 3  //3 nodes and 3 edges
# 1 2 5 //node1-node2-cost
# 2 3 8
# 1 3 3


node, edge = map(int, input().split())
# adj_mat = [[0 for i in range(node + 1)]]*(node + 1)
adj_mat = [[0] * (node + 1) for i in range(node + 1)]
for e in range(edge):
    node1, node2, cost = map(int, input().split())
    adj_mat[node1][node2] = cost
    adj_mat[node2][node1] = cost

for i in range(1, node + 1):
    for j in range(1, node + 1):
        print(adj_mat[i][j], end=" ")
    print()

# The line adj_mat = [[0 for i in range(node + 1)]] * (node + 1) creates a list with node + 1 references to the same inner list [0 for i in range(node + 1)].
# This is a shallow copy, meaning that if you modify one of the inner lists, the changes will be reflected in all the other inner lists
# because they reference the same list object. adj_mat = [[0 for i in range(node + 1)] for j in range(node + 1)]

