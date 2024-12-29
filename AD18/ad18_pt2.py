from collections import deque
import heapq
from PIL import Image

def main():
    with open('ad18.txt') as f:
        lines = f.readlines()

    # Split lines into list of tuples
    total_coordinates = [tuple(map(int, line.strip().split(','))) for line in lines]
    map_size = 71
        
    # Create a map of the coordinates
    map_wh = [[0 for x in range(map_size)] for y in range(map_size)]

    # Go through each coordinate
    for i in range(len(total_coordinates)):
        coordinates = total_coordinates[:i+1]

        # Save coord
        coord = coordinates[i]
        
        # Put coord on map (1 = blocked)
        map_wh[coord[1]][coord[0]] = 1

        # Solve the maze with current coordinates
        path = solve(map_wh)
        
        # If no path found, print message and break (this is solution for part 2, the coord that breaks the path)
        if path is None:
            print(f"No path found: coord: {coord}")
            break
        else:
            print(f"Path length: {len(path) - 1}")


# Function used find manhattan distance between two coordinates
def distance(coord_1, coord_2):
    return abs(coord_1[0] - coord_2[0]) + abs(coord_1[1] - coord_2[1])

# Function used to solve the maze using A* algorithm
def solve(map_wh):
    start = (0, 0)
    end = (len(map_wh[0]) - 1, len(map_wh) - 1)

    # Ensure start and end points are valid
    if map_wh[start[1]][start[0]] != 0 or map_wh[end[1]][end[0]] != 0:
        print("Start or end point is blocked")
        return None

    queue = []
    heapq.heappush(queue, (0 + distance(start, end), 0, start, [start]))
    visited_coords = set()
    visited_coords.add(start)
    
    while queue:
        _, cost, current, path = heapq.heappop(queue)

        if current == end:
            return path

        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for move in moves:
            new_coord = (current[0] + move[0], current[1] + move[1])

            # Check if new_coord is within bounds and not already visited
            if (
                0 <= new_coord[0] < len(map_wh[0]) and
                0 <= new_coord[1] < len(map_wh) and
                new_coord not in visited_coords and
                map_wh[new_coord[1]][new_coord[0]] == 0
            ):
                visited_coords.add(new_coord)
                new_path = path + [new_coord]
                new_cost = cost + 1
                priority = new_cost + distance(new_coord, end)
                heapq.heappush(queue, (priority, new_cost, new_coord, new_path))

    return None

if __name__ == "__main__":
    main()
