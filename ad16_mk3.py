import csv
import sys
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

sys.setrecursionlimit(10000)

def main():
    print("Start")
    filename = "ad16_test.csv"
    map_wh, start_coord, end_coord = open_csv(filename)

    # Create graph
    graph_coords = nx.Graph()
    visited_coords = []
    moves = []
    
    bfs_solve_maze(map_wh, start_coord, visited_coords, moves, graph_coords, end_coord)
    
    for coord in visited_coords:
        map_wh[coord[0]][coord[1]] = "■"
        
    for row in map_wh:
        print("".join(row))
        
    cost = calc_path_score(visited_coords)

    print(moves)
    print(cost)
    
    # Use nx.planar_layout to calculate positions
    pos = nx.planar_layout(graph_coords)
    
    # Draw the graph with the computed planar layout
    nx.draw(graph_coords, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
    
    # Draw edge labels (weights)
    edge_labels = nx.get_edge_attributes(graph_coords, 'weight')
    nx.draw_networkx_edge_labels(graph_coords, pos, edge_labels=edge_labels, font_size=8)
    
    plt.show()


def bfs_solve_maze(map_wh, start_coord, visited_coords, path, graph_coords, end_coord):
    queue = deque([(start_coord, [])])  # Store (current_coord, current_path)
    visited = set()
    
    while queue:
        current_coord, current_path = queue.popleft()
        x, y = current_coord
        
        if current_coord in visited or map_wh[x][y] == "#":
            continue
        
        visited.add(current_coord)
        visited_coords.append(current_coord)
        
        if current_coord == end_coord:
            path.extend(current_path)
            break

        # Define moves with corresponding directions
        moves = [
            ((0, 1), "right"),
            ((0, -1), "left"),
            ((-1, 0), "up"),
            ((1, 0), "down")
        ]

        for move, direction in moves:
            next_coord = (x + move[0], y + move[1])
            if next_coord not in visited:
                queue.append((next_coord, current_path + [direction]))
                cost = 1 if current_path and current_path[-1] == direction else 1000
                graph_coords.add_weighted_edges_from([(current_coord, next_coord, cost)])


def calc_path_score(path_coords):
    old_coord = path_coords[0]
    directions = []
    for coord_i, coord in enumerate(path_coords):
        if coord_i == 0:
            continue
        
        if old_coord[0] != coord[0]:
            directions.append(1)
            
        if old_coord[1] != coord[1]:
            directions.append(0)

        old_coord = coord
    
    turns = 1  
    # Count turns
    for i in range(1, len(directions)):
        if directions[i] != directions[i - 1]: 
            turns += 1
    print(directions)
    print(f"Turns: {turns} Straight: {len(directions)}")
    cost = len(directions) + turns * 1000
    
    return cost


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
