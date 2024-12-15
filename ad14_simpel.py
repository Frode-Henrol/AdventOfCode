import matplotlib.pyplot as plt
import os

def main():
    filename = "ad14.txt"
    start_robot_list = load_txt(filename)
    row_size = 103
    col_size = 101
        
    #row_size = 7
    #col_size = 9
    oldsf = float("inf")
    
    # Change to 100 to solve part1
    moves = 100000000
    for move in range(moves + 1):
        map = [[0] * col_size for _ in range(row_size)]
        for robot_nr in range(len(start_robot_list)):
            pos, vel = start_robot_list[robot_nr]

            col, row = pos
            v_col, v_row = vel
            row, col = (row + v_row * move) % row_size, (col + v_col * move) % col_size

            if map[row][col] != 0:
                map[row][col] += 1
            else:
                map[row][col] = 1

        sf = safety_factor(map)
        
        # For part2 look for least sf scores and print. Tree could be inside the zone were tiles are ignored
        if sf < oldsf:
            oldsf = sf
            save_map_as_image(map, move)
        
    
        print(sf)
        
def save_map_as_image(map, move):
    # Ensure the folder exists
    folder_name = "ad14pt2_pics"
    os.makedirs(folder_name, exist_ok=True)  # Creates the folder if it doesn't exist

    # Convert the map to a visual representation
    plt.figure(figsize=(8, 8))
    plt.imshow(map, cmap='viridis', origin='upper')
    plt.colorbar(label="Robot Density")
    plt.title(f"Map at Move {move}")
    plt.xlabel("Columns")
    plt.ylabel("Rows")

    # Save the image with a unique name for each move in the specified folder
    file_path = os.path.join(folder_name, f"map_move_{move}.png")
    plt.savefig(file_path)
    plt.close()
    
def safety_factor(map):
    row_length = len(map)
    col_length = len(map[0])

    # Find the middle row and column (ignore if uneven)
    mid_row = row_length // 2
    mid_col = col_length // 2

    # Split the map into quadrants
    quadrants = []
    quadrants.append([row[:mid_col] for row in map[:mid_row]])
    quadrants.append([row[mid_col + 1:] for row in map[:mid_row]])
    quadrants.append([row[:mid_col] for row in map[mid_row + 1:]])
    quadrants.append([row[mid_col + 1:] for row in map[mid_row + 1:]])

    safety_factor_list = []
    for quadrant in quadrants:
        safety_factor_num = 0
        for row in quadrant:
            for num in row:
                safety_factor_num += num

        safety_factor_list.append(safety_factor_num)
    result = 1
    for num in safety_factor_list:
        result *= num

    return result

def load_txt(filename):
    robot_list = []
    with open(filename, "r") as file:
        for row in file:
            parts = row.split()
            p = tuple(map(int, parts[0].split('=')[1].split(',')))
            v = tuple(map(int, parts[1].split('=')[1].split(',')))

            #print(p, v)
            robot_list.append((p, v))

    return robot_list

if __name__ == "__main__":
    main()
