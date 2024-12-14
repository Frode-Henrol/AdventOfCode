import csv
import time


def main():
    start_time = time.time()  # Record the start time
    # Open csv and make farm map
    filename = "ad12.csv"
    farm_map = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            farm_map.append(list(row[0]))

                
    total_price = 0
    for row in range(len(farm_map)):
        for col in range(len(farm_map[0])):
            coord = (row, col)
            if farm_map[row][col] != "#":
                crop_type = farm_map[row][col]
                fences_total, crops_total = search_field(farm_map, coord, crop_type)
                total_price += fences_total*crops_total
    
    end_time = time.time()  # Record the end time
    execution_time = end_time - start_time
    print(f"{total_price}, {execution_time:.6f}s")
    
def search_field(farm_map, coord, crop_type):
    row, col = coord
    farm_map[row][col] = "#"
    neighbor_offsets = [ (-1, 0), (1, 0), (0, -1), (0, 1) ]
    
    fences_total = 0
    crops_total = 1
    
    # Check neighbors
    for row, col in neighbor_offsets:
        new_coord = (coord[0] + row, coord[1] + col)
        n_row, n_col = new_coord
        
        if len(farm_map)>n_row>=0 and len(farm_map[0])>n_col>=0 and farm_map[n_row][n_col] == crop_type:

            if farm_map[col][row] != "#":
                fences, crops = search_field(farm_map, new_coord, crop_type)
                crops_total += crops
                fences_total +=fences
        else:
            fences_total+=1
     

     
    return fences_total, crops_total 


def check_neighbors():
    pass



if __name__ == "__main__":
    main()
    


    