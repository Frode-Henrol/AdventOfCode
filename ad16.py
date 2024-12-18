import csv
import copy
import sys
sys.setrecursionlimit(10000)

def main():
    print("Start")
    #filename = "ad16_test.csv"
    filename = "ad16.csv"
    map_wh, start_coord, end_coord = open_csv(filename)

    

    visited_coords = []
    solve_maze(map_wh, start_coord, visited_coords)
    
    for coord in visited_coords:
        map_wh[coord[0]][coord[1]] = "■"
        
    for row in map_wh:
        print("".join(row))
        
    cost = calc_path_score(visited_coords)

    print(cost)
    

def solve_maze(map_wh: list, coord: tuple, visited_coords: list):
    x, y = coord
    
    if coord in visited_coords or map_wh[x][y] == "#":
        return False
    
    if map_wh[x][y] == "E":
        visited_coords.append(coord)
        return True

    visited_coords.append(coord)

    moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    for move in moves:
        next_coord = (x + move[0], y + move[1])
        if solve_maze(map_wh, next_coord, visited_coords):
            return True

    # If no path is found, backtrack
    visited_coords.pop()
    return False

    

def calc_path_score(path_coords: list):
    
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