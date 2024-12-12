def count_external_sides(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    total_sides = 0
    shared_sides = 0

    # Iterate through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'A':
                total_sides += 4  # Each 'A' contributes 4 potential sides

                # Check right neighbor
                if j + 1 < cols and grid[i][j + 1] == 'A':
                    shared_sides += 1

                # Check bottom neighbor
                if i + 1 < rows and grid[i + 1][j] == 'A':
                    shared_sides += 1

    # Calculate external sides
    external_sides = total_sides - (2 * shared_sides)
    return external_sides

# Example usage
grid = [
    ['A', 'A', 'A', 'A', 'X'],
    ['A', 'A', 'X', 'A', 'X'],
    ['A', 'A', 'A', 'A', 'A'],
    ['X', 'X', 'A', 'X', 'X']
]

external_sides = count_external_sides(grid)
print(f"Number of external sides: {external_sides}")
