import numpy as np
from sys import maxsize
from itertools import permutations

V = 4 # Number of vertices
graph = np.array([[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]])
source = 0

other_vertices = [i for i in range(V) if i != source]
min_path = maxsize
path_permutations = permutations(other_vertices)
for path_permutation in path_permutations:
    current_pathweight = 0 # current pathweight
    i = source
    for j in path_permutation:
        current_pathweight += graph[i, j]
        i = j

    # return to the source vertex
    current_pathweight += graph[i, source]
    if current_pathweight < min_path:
        optimal_path = path_permutation
    min_path = min(min_path, current_pathweight)
print(f"Optimal pathweight: {min_path}")
optimal_path = [source] + list(optimal_path)
print("Optimal path: " + str(optimal_path))
