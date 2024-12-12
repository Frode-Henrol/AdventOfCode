import csv

def main():
    # Open csv and make farm map
    filename = "ad12.csv"
    farm_map = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            farm_map.append(list(row[0]))

                
    visited_coords = set()
    total_price = 0
    for row in range(len(farm_map)):
        for col in range(len(farm_map[0])):
            coord = (row, col)
            if coord not in visited_coords:
                crop_type = farm_map[row][col]
                fences_total, crops_total = search_field(farm_map, coord, visited_coords, crop_type)
                total_price += fences_total*crops_total
    
    print(total_price)
        
def search_field(farm_map, coord, visited_coords, crop_type):
    visited_coords.add(coord)
    neighbor_offsets = [ (-1, 0), (1, 0), (0, -1), (0, 1) ]
    
    fences_total = 0
    crops_total = 1
    
    # Check neighbors
    for row, col in neighbor_offsets:
        new_coord = (coord[0] + row, coord[1] + col)
        n_row, n_col = new_coord
        
        if len(farm_map)>n_row>=0 and len(farm_map[0])>n_col>=0 and farm_map[n_row][n_col] == crop_type:

            if new_coord not in visited_coords:
                fences, crops = search_field(farm_map, new_coord, visited_coords, crop_type)
                crops_total += crops
                fences_total +=fences
        else:
            fences_total+=1
     
    return fences_total, crops_total 
            

if __name__ == "__main__":
    main()
    


    