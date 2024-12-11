import csv

def main():
    # Import csv
    trail_start_coords, hike_map = import_csv()

    
    total_sum1 = 0
    for start_coord in trail_start_coords:
        visited_peaks1 = []
        visited_coord1 = []
        total_sum1 += search_part1(start_coord, hike_map, visited_coord1, visited_peaks1)

    print(f"Part 1: {total_sum1}")

    total_sum2 = 0
    for start_coord in trail_start_coords:
        visited_coord2 = []
        total_sum2 += search_part2(start_coord, hike_map, visited_coord2)
    
    print(f"Part 2: {total_sum2}")

#----------------------------------------------------
#-
#---------------------------------------------------- 
def import_csv():
    trail_start_coords = []
    hike_map = []
    
    with open("ad10.csv", "r") as file:
        reader = csv.reader(file)
        for row_index, row in enumerate(reader):
            
            hike_map.append(list(row[0]))
            
            for col_index, col in enumerate(row[0]):
                if col == "0":
                    trail_start_coords.append((row_index,col_index))
     
    return trail_start_coords, hike_map              
#----------------------------------------------------
#-
#---------------------------------------------------- 
def search_part1(coord, map, visited_coord, visited_peaks):
    visited_coord.append(coord)

    neighbor_offsets = [ (-1, 0), (1, 0), (0, -1), (0, 1) ]
    
    total_sum = 0  # Initialize sum for this level
    
    # Check neighbors
    for row, col in neighbor_offsets:
        new_coord = (coord[0] + row, coord[1] + col)
        n_row, n_col = new_coord
        
        # Check next move is within bounds and not visisted
        if new_coord not in visited_coord and len(map)> n_row >=0 and 0 <= n_col<len(map) :
            
            # Check if next move i 1+ in height
            heigt_diff = int(map[n_row][n_col]) - int(map[coord[0]][coord[1]])
            if heigt_diff != 1:
                continue
            
            # Check if peak is reached and we have not visited it before
            if map[n_row][n_col] == "9" and (n_row,n_col) not in visited_peaks:
                visited_peaks.append((n_row,n_col))
                total_sum += 1  
            # If not a peak step further into trail be calling search again
            else:
                total_sum += search_part1(new_coord, map, visited_coord, visited_peaks)
                
    return total_sum
#----------------------------------------------------
#-
#---------------------------------------------------- 
def search_part2(coord, map, visited_coord):
    
    # If we reach end of route return 1
    if map[coord[0]][coord[1]] == "9":
        return 1

    neighbor_offsets = [ (-1, 0), (1, 0), (0, -1), (0, 1) ]
    total_routes = 0  # Initialize sum for this level
    
    # Check neighbors
    for row, col in neighbor_offsets:
        new_coord = (coord[0] + row, coord[1] + col)
        n_row, n_col = new_coord
        
        # Check next move is within bounds and not visisted
        if new_coord not in visited_coord and len(map)> n_row >=0 and 0 <= n_col<len(map) :
            
            # Check if next move i 1+ in height
            heigt_diff = int(map[n_row][n_col]) - int(map[coord[0]][coord[1]])
            
            # If move is valid go to next
            if heigt_diff == 1:
                total_routes += search_part2(new_coord, map, visited_coord)
                
    return total_routes


if __name__ == "__main__":
    main()
