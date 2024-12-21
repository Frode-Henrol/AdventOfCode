import csv
import sys
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import copy
from collections import defaultdict

sys.setrecursionlimit(10000)

def main():
    print("Start")
    filename = "ad16_test.csv"
    map_wh, start_coord, end_coord = open_csv(filename)

    map_wh_mk2, graph_dic = cost_map(map_wh)

    graphNX = nx.Graph()

    # Add nodes with their weights
    for node, neighbors in graph_dic.items():
        graphNX.add_node(node)  # Set node weight based on map_wh_mk2

    # Add edges between neighbors
    for node, neighbors in graph_dic.items():
        for neighbor in neighbors:
            graphNX.add_edge(node, neighbor, weight=map_wh_mk2[node[0]][node[1]])

    # Find the shortest path based on node weights
    try:
        shortest_path = nx.dijkstra_path(graphNX, start_coord, end_coord, weight='weight')
        print(f"Shortest path from {start_coord} to {end_coord}: {shortest_path}")
        
        # Mark the path on the map
        cost = -1
        cost_path = []
        for coord in shortest_path:
            map_wh[coord[0]][coord[1]] = "■"
            cost_path.append((map_wh_mk2[coord[0]][coord[1]], coord))
            cost += map_wh_mk2[coord[0]][coord[1]]


        # Print the updated map with the path marked
        for row in map_wh:
            print("".join(row))

    except nx.NetworkXNoPath:
        print("No path found.")


        cost = 0
        cost_path = []
        for i in range(len(shortest_path) - 2):
            prev_coord = shortest_path[i]
            curr_coord = shortest_path[i + 1]
            next_coord = shortest_path[i + 2]

            # Calculate direction of movement
            prev_direction = (curr_coord[0] - prev_coord[0], curr_coord[1] - prev_coord[1])
            next_direction = (next_coord[0] - curr_coord[0], next_coord[1] - curr_coord[1])

            # Check if there's a turn
            if prev_direction != next_direction:
                step_cost = map_wh_mk2[curr_coord[0]][curr_coord[1]]  # Use 1001 for intersections
            else:
                step_cost = 1  # No additional cost for straight movement

            cost += step_cost
            cost_path.append((step_cost, curr_coord))
            map_wh[curr_coord[0]][curr_coord[1]] = "■"

    print(f"Cost path: {cost_path} path steps: {len(cost_path)}")
    print(f"Cost: {cost}")

                
def cost_map(map_wh: list):
    # make cost function
    graph_dic = defaultdict(list)
    cost_map_wh = copy.deepcopy(map_wh) # Used to calc corners
    map_wh_mk2 = [[0 if cell == "#" else 1 for cell in row] for row in map_wh] # Final map with costs
    
    # Run throug 3x3 grid
    for row_i in range(1, len(map_wh_mk2) - 1):
        for col_i in range(1, len(map_wh_mk2[0]) - 1):
            if map_wh_mk2[row_i][col_i] != 0:
                
                # Extract middle row and col
                sub_grid_col = map_wh_mk2[row_i][col_i-1:col_i+2]
                sub_grid_row = [row[col_i] for row in map_wh_mk2[row_i-1:row_i+2]]

                #print(sub_grid_col, sub_grid_row)
                
                # Make all straights (1)
                if cost_map_wh[row_i][col_i] == ".":
                    cost_map_wh[row_i][col_i] = 1

                # Detect corners/intersections (1000)
                if sum(sub_grid_col) == 2 and sum(sub_grid_row) == 2:
                    map_wh_mk2[row_i][col_i] = 1001
                if sum(sub_grid_col) == 3 and sum(sub_grid_row) == 3:
                    map_wh_mk2[row_i][col_i] = 1001
                if (sum(sub_grid_col) == 3 and sum(sub_grid_row) == 2) or (sum(sub_grid_col) == 2 and sum(sub_grid_row) == 3):
                    map_wh_mk2[row_i][col_i] = 1001

    # Make dic with neighbors and there cost
    for row_i in range(1, len(map_wh_mk2) - 1):
        for col_i in range(1, len(map_wh_mk2[0]) - 1):
            if map_wh_mk2[row_i][col_i] != 0:
                for move_row, move_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    new_row, new_col = row_i + move_row, col_i + move_col
                    if map_wh_mk2[new_row][new_col] != 0:
                        #if map_wh_mk2[new_row][new_col] != 0:
                        #print(f"COST costmap: {map_wh_mk2[new_row][new_col]}")
                        #print(f"COST wh2: {map_wh_mk2[new_row][new_col]}")
                        graph_dic[(row_i, col_i)].append((new_row, new_col))
                        #graph_dic[(row_i, col_i)].append(((new_row, new_col), cost_map_wh[new_row][new_col]))

    for node, neighbors in graph_dic.items():
        print(f"Node {node} connects to {neighbors}")
    
    print(f"Costmap")
    for row in cost_map_wh:
        print(row)

    print(f"map_wh_mk2")
    for row in map_wh_mk2:
        print(row)


    return map_wh_mk2, graph_dic


def open_csv(filename: str):
    map_wh = []
    
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row_i, row in enumerate(reader):
            map_wh.append(list(row[0]))
            for col_i, col in enumerate(row[0]):
                if col == "S":
                    start_coord = (row_i, col_i)
                if col == "E":
                    end_coord = (row_i, col_i)
    return map_wh, start_coord, end_coord


if __name__ == "__main__":
    main()
