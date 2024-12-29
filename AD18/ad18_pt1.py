from collections import deque
import heapq
from PIL import Image

def main():
    with open('ad18.txt') as f:
        lines = f.readlines()

    # Split lines into list of tuples
    coordinates = [tuple(map(int, line.strip().split(','))) for line in lines]
    amount = 1024
    coordinates = coordinates[:amount]

    map_size = 6
    
    # Create a map of the coordinates
    map_wh = [[0 for x in range(map_size)] for y in range(map_size)]

    for coord in coordinates:
        map_wh[coord[1]][coord[0]] = 1

    path = solve(map_wh)

    if path is None:
        print("No path found")
    else:
        print(len(path) - 1)
        for coord in path:
            map_wh[coord[1]][coord[0]] = 2
        
        save_maze_image(map_wh, "maze_with_path.png", show_path=True)
    
    save_maze_image(map_wh, "maze_without_path.png", show_path=False)

def distance(coord_1, coord_2):
    return abs(coord_1[0] - coord_2[0]) + abs(coord_1[1] - coord_2[1])

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

def save_maze_image(map_wh, filename, show_path):
    height = len(map_wh)
    width = len(map_wh[0])

    # Create an image with RGB mode
    img = Image.new("RGB", (width, height))
    pixels = img.load()

    for y in range(height):
        for x in range(width):
            if map_wh[y][x] == 1:  # Wall
                pixels[x, y] = (0, 0, 0)  # Black
            elif map_wh[y][x] == 2 and show_path:  # Path
                pixels[x, y] = (0, 0, 255)  # Blue
            else:  # Empty space
                pixels[x, y] = (255, 255, 255)  # White

    img.save(filename)

if __name__ == "__main__":
    main()
