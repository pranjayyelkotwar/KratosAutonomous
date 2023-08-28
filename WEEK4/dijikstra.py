from math import sqrt
from matplotlib.colors import ListedColormap
import numpy as np
import matplotlib.pyplot as plt
import time

def valid_node(node, size_of_grid):
    """Checks if node is within the grid boundaries."""
    if node[0] < 0 or node[0] >= size_of_grid:
        return False
    if node[1] < 0 or node[1] >= size_of_grid:
        return False
    if obstacles[node[0], node[1]] != 0:
        print(f'{node} this is a fucking obstacle')
        return False
    return True

def sqrtdist(point1, point2):
    return sqrt(pow((point1[0] - point2[0]), 2) + pow((point1[1] - point2[1]), 2))

def up(node):
    return (node[0] - 1, node[1])

def down(node):
    return (node[0] + 1, node[1])

def left(node):
    return (node[0], node[1] - 1)

def right(node):
    return (node[0], node[1] + 1)

def backtrack(initial_node, desired_node, distances):
    path = [desired_node]
    size_of_grid = distances.shape[0]

    while True:
        potential_distances = []
        potential_nodes = []

        directions = [up, down, left, right]

        for direction in directions:
            node = direction(path[-1])
            if valid_node(node, size_of_grid):
                if obstacles[node[0], node[1]] == 0:
                    potential_nodes.append(node)
                    potential_distances.append(distances[node[0], node[1]])

        least_distance_index = np.argmin(potential_distances)
        path.append(potential_nodes[least_distance_index])

        if path[-1][0] == initial_node[0] and path[-1][1] == initial_node[1]:
            break
    return list(reversed(path))

def dijkstra(initial_node, desired_node, obstacles):
    obstacles = obstacles.copy()
    obstacles *= 1000
    obstacles += np.ones(obstacles.shape)
    obstacles[initial_node[0], initial_node[1]] = 0
    obstacles[desired_node[0], desired_node[1]] = 0

    size_of_floor = obstacles.shape[0]
    visited = np.zeros([size_of_floor, size_of_floor], bool)
    distances = np.ones([size_of_floor, size_of_floor]) * np.inf
    distances[initial_node[0], initial_node[1]] = 0

    current_node = initial_node

    while True:
        print(f'currently at {current_node}')
        directions = [up, down, left, right]
        for direction in directions:
            potential_node = direction(current_node)
            if valid_node(potential_node, size_of_floor):
                if not visited[potential_node[0], potential_node[1]] and obstacles[potential_node[0], potential_node[1]] < 1000:
                    distance = distances[current_node[0], current_node[1]] + obstacles[potential_node[0], potential_node[1]]
                    if distance < distances[potential_node[0], potential_node[1]]:
                        distances[potential_node[0], potential_node[1]] = distance

        visited[current_node[0], current_node[1]] = True

        t = distances.copy()
        t[np.where(visited)] = np.inf
        node_index = np.argmin(t)
        node_row = node_index // size_of_floor
        node_col = node_index % size_of_floor
        current_node = (node_row, node_col)

        if current_node[0] == desired_node[0] and current_node[1] == desired_node[1]:
            break

    return backtrack(initial_node, desired_node, distances)

obstacles =np.array([
 [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
 [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
 [1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
 [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
 [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
 [1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1],
 [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
 [1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1],
 [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
 [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
 [1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0]
]
,dtype=float)
path = dijkstra([19,19], [3,1], obstacles)
print(path)
colors = ['white', 'black']
cmap = ListedColormap(colors)

plt.imshow(obstacles, cmap=cmap, interpolation='nearest')
plt.draw()
plt.pause(2)
colors.append('red')
cmap = ListedColormap(colors)
plt.imshow(obstacles, cmap=cmap, interpolation='nearest')
for node in path:
    if obstacles[node[0], node[1]] == 1:
        continue
    obstacles[node[0], node[1]] = 2
    plt.imshow(obstacles, cmap=cmap, interpolation='nearest')
    plt.draw()
    plt.pause(0.1)

time.sleep(5)
p = np.zeros(shape=obstacles.shape)

for i in range(len(path)):
    p[path[i][0], path[i][1]] = np.nan
