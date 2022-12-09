# This program uses dynamic programing to solve TSP problem
from sys import maxsize
from itertools import permutations

# number of nodes
n = int(input())

# matrix representation of graph
graph = [list(map(int, input().split())) for _ in range(n)]

# function to implement TSP


def TSP(graph, s):

    # keep all vertex other than the starting point
    vertex = []

    # traverse the diagram
    for i in range(n):
        if i != s:
            vertex.append(i)

    # keep minimum weight
    min_path = maxsize

    next_permutation = permutations(vertex)
    best_path = []

    for i in next_permutation:
        # store current Path weight(cost)
        current_pathweight = 0

        # compute current path weight
        k = s

        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]

        # update minimum
        if current_pathweight < min_path:
            min_path = current_pathweight
            best_path = [s]
            best_path.extend(list(i))
            best_path.append(s)

    return min_path, best_path


s = 0

print(TSP(graph, s))


# input
# 5
# 0 0 0 1000 1000
# 0 0 20 28 30
# 0 25 0 27 28
# 1000 30 35 0 29
# 1000 28 29 27 0

#   [0 20 28 30 0],
#   [25 0 27 28 0],
#   [30 35 0 29 1000],
#   [28 29 27 0 1000],
#   [0 0 1000 1000 0]
