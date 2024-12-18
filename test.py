from collections import deque

def calculate_distances(grid):
    # Convert the input into a mutable grid
    grid = [list(row) for row in grid]

    # Find the starting point 'S'
    start = None
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == 'S':
                start = (r, c)
                break
        if start:
            break

    if not start:
        raise ValueError("Starting point 'S' not found in the grid")

    # Initialize the distance grid
    rows, cols = len(grid), len(grid[0])
    distances = [[-1 if cell == '.' else cell for cell in row] for row in grid]

    # BFS setup
    queue = deque([start])
    distances[start[0]][start[1]] = 0

    # Directions for moving in the grid (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.popleft()
        current_distance = distances[x][y]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # Check if the next position is within bounds and is a '.'
            if 0 <= nx < rows and 0 <= ny < cols and distances[nx][ny] == -1:
                distances[nx][ny] = current_distance + 1
                queue.append((nx, ny))

    # Convert distances back to strings for printing
    for r in range(rows):
        for c in range(cols):
            if isinstance(distances[r][c], int):
                grid[r][c] = str(distances[r][c])

    return ["".join(row) for row in grid]

# Example grid
grid = [
    "###############",
    "#.......#....E#",
    "#.#.###.#.###.#",
    "#.....#.#...#.#",
    "#.###.#####.#.#",
    "#.#.#.......#.#",
    "#.#.#####.###.#",
    "#...........#.#",
    "###.#.#####.#.#",
    "#...#.....#.#.#",
    "#.#.#.###.#.#.#",
    "#.....#...#.#.#",
    "#.###.#.#.#.#.#",
    "#S..#.....#...#",
    "###############"
]

# Calculate distances and print the result
result = calculate_distances(grid)
for row in result:
    print(list(row))