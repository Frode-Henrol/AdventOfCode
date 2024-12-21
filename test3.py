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

    cost_map_wh, graph_dic = cost_map(map_wh)

    graphNX = nx.Graph()

    # Add nodes with their weights, based on the cost_map_wh
    for node, neighbors in graph_dic.items():
        graphNX.add_node(node, weight=cost_map_wh[node[0]][node[1]])  # Assign node weight here
        for neighbor, _ in neighbors:
            graphNX.add_edge(node, neighbor)  # No edge weight needed

    showplot = False
    if showplot:
        # Visualize the graph (optional)
        import matplotlib.pyplot as plt
        pos = nx.spring_layout(graphNX)  # Layout for visualization
        nx.draw(graphNX, pos, with_labels=True, node_color='lightblue', font_weight='bold')
        labels = nx.get_edge_attributes(graphNX, 'weight')  # Get edge weights (which will be empty in this case)
        nx.draw_networkx_edge_labels(graphNX, pos, edge_labels=labels)
        plt.show()

    # Run Dijkstra's algorithm on nodes with their weights as cost
    path = nx.dijkstra_path(graphNX, source=start_coord, target=end_coord, weight='weight')
    print("Shortest path using Dijkstra (node weights):", path)

    for coord in path:
        map_wh[coord[0]][coord[1]] = "■"

    # Output the map with the path marked
    for row in map_wh:
        print("".join(row))


def cost_map(map_wh: list):
    # Create cost map for nodes
    graph_dic = defaultdict(list)
    cost_map_wh = copy.deepcopy(map_wh)
    map_wh_mk2 = [[0 if cell == "#" else 1 for cell in row] for row in map_wh]
    
    # Build cost map and neighbor relationships
    for row_i in range(1, len(map_wh_mk2) - 1):
        for col_i in range(1, len(map_wh_mk2[0]) - 1):
            if map_wh_mk2[row_i][col_i] != 0:
                
                # Make all straights (1)
                if cost_map_wh[row_i][col_i] == ".":
                    cost_map_wh[row_i][col_i] = 1

                # Detect corners/intersections (1000)
                if sum(map_wh_mk2[row_i][col_i-1:col_i+2]) == 2 and sum([row[col_i] for row in map_wh_mk2[row_i-1:row_i+2]]) == 2:
                    cost_map_wh[row_i][col_i] = 1000

    # Add neighbors to graph
    for row_i in range(1, len(map_wh_mk2) - 1):
        for col_i in range(1, len(map_wh_mk2[0]) - 1):
            for move_row, move_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row, new_col = row_i + move_row, col_i + move_col
                if cost_map_wh[new_row][new_col] != "#":  # Valid cell
                    graph_dic[(row_i, col_i)].append(((new_row, new_col), cost_map_wh[new_row][new_col]))  # Neighbors
    
    return cost_map_wh, graph_dic


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
