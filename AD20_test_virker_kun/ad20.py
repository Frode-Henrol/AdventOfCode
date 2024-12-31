from collections import defaultdict
import sys
sys.setrecursionlimit(10000)

# Udmiddelbart er fejlen at jeg kun at kodet den til at snyde igennem 1 lags vægge, men den skal kune igennem 2 lags vægge


def main():
    # Load map
    filename = "ad20.txt"
    with open(filename) as f:
        data = f.read().split("\n")

    map_wh = [list(row) for row in data]

    # Find start and end coordinates
    start = None
    end = None
    for y, row in enumerate(map_wh):
        for x, char in enumerate(row):
            if char == 'S':
                start = (y, x)
            elif char == 'E':
                end = (y, x)

    print(f"Start: {start}, End: {end}")

    # Find the path from start to end
    path = find_path(start, map_wh, set([start]), end)
    
    
    #print(f"Path is: {path}")

    if path:
        # Mark the path on the map

        #for coord in path:
        #    map_wh[coord[0]][coord[1]] = "X"  # Note: coordinates are (x, y)

        # Print the map with the path
        for row in map_wh:
            print("".join(row))
    else:
        print("No path found")


    coord_to_remove = []

    # Find coord and the coord that can be cheated to
    used_coords = []
    for coord in path:
        list_cheat = find_cheat_coord_pair(coord, map_wh, path, used_coords)
        for cheat in list_cheat:
            coord_to_remove.append(cheat)

    #print(coord_to_remove)
    #print(f"Path length: {len(path)-1}")

    storing_dic = find_new_path_length(path, coord_to_remove)

    #for key, value in storing_dic.items():
    #    print(f"Key: {key}, Value: {value}")

    print(f"Path length: {len(path)-1}")
    print(f"part 1: {storing_dic[100]}")

    # need to give 1497 for part 1 ????
    


def find_new_path_length(path, coord_to_remove):
    storing_dic = defaultdict(int)
    original_len = len(path)-1

    for coord in coord_to_remove:
        try:
            # Find index of cheated coord in path
            index_cheat = path.index(coord[1])
            # Find index of coord before chead in path
            index_orig = path.index(coord[0])
        except:
            continue
        
        # skal fixes så det passer med eksempel???? - fordi hvis et coord har flere cheats, dette kan den ikke forstår se path index 18
        storing_dic[index_cheat - index_orig-2] += 1
        #print(f"{index_orig} - {index_cheat} with diff: {index_cheat - index_orig-2}")

    return storing_dic


def find_cheat_coord_pair(current_coord, map_wh, path, used_coords):
    #print(f"-----Looking at coord {current_coord}-----")

    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    valid_cheats = []    

    for move in moves:
        new_coord_one = (current_coord[0] + move[0], current_coord[1] + move[1])
        new_coord_two = (current_coord[0] + move[0] * 2, current_coord[1] + move[1] * 2)
    
        if 0 <= new_coord_two[0] < len(map_wh) and 0 <= new_coord_two[1] < len(map_wh[0]):
            if map_wh[new_coord_one[0]][new_coord_one[1]] == "#" and map_wh[new_coord_two[0]][new_coord_two[1]] != "#":
                if new_coord_two in path and new_coord_two not in used_coords:
                    #print(f"neighbor at {new_coord_two} with content: {map_wh[new_coord_two[0]][new_coord_two[1]]}")
                    # Check if the coord has been used before
                    valid_cheats.append((current_coord, new_coord_two))
    used_coords.append(current_coord)   # - causes problem since i can't use the same coord twice and a coord can have multiple cheats        
    return valid_cheats


def find_path(current_coord, map_wh, visited_coords, end_coord):
    # Base case: if we've reached the end, return the path
    if current_coord == end_coord:
        return [current_coord]
    
    # Possible moves: right, left, down, up
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    for move in moves:
        new_coord = (current_coord[0] + move[0], current_coord[1] + move[1])
        # Check if the new coordinates are valid and not visited
        if is_valid_move(new_coord, map_wh, visited_coords):
            visited_coords.add(new_coord)
            path = find_path(new_coord, map_wh, visited_coords, end_coord)
            
            # If a valid path is found, append current coordinate to the path and return
            if path:
                return [current_coord] + path
    
    return None


def is_valid_move(coord, map_wh, visited_coords):
    # Check if the coordinate is within bounds, not a wall, and not visited
    row, col = coord
    if 0 <= col < len(map_wh) and 0 <= row < len(map_wh[0]):
        if map_wh[row][col] != "#" and coord not in visited_coords:
            return True
    return False

if __name__ == "__main__":
    main()  