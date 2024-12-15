import csv


def main():

    filename = "ad15_test.csv"
    map_wh, controls, start_coord = load_csv(filename)
    for row in map_wh:
        print(row)
        
    print(controls)
    print(start_coord)
    coord = start_coord

    for control in controls:
        print(f"Control used: {control}")
        if control == "^":
            move = (-1, 0)
        elif control == "v":
            move = (1, 0)
        elif control == "<":
            move = (0, -1)
        elif control == ">":
            move = (0, 1)
            
        coord_row, coord_col = coord
        move_row, move_col = move
        new_row, new_col = coord_row + move_row, coord_col + move_col
        
        next_tile = map_wh[new_row][new_col]
        if next_tile == ".":
            coord = new_row, new_col
            map_wh[coord_row][coord_col] = map_wh[new_row][new_col]
            map_wh[new_row][new_col] = "@"
            
        elif next_tile == "O":
            iter = 0
            while True:
                iter += 1
                new_row, new_col = coord_row + move_row, coord_col + move_col
                newnew_row, newnew_col = coord_row + move_row * iter, coord_col + move_col * iter
                if map_wh[newnew_row][newnew_col] == ".":
                    print(f"Free space behind box {new_row} {new_col}")
                    
                    # Swap next tile (box) with the next free space.
                    map_wh[new_row][new_col] = map_wh[newnew_row][newnew_col]
                    coord = new_row, new_col
                    break
                    
                elif map_wh[newnew_row][newnew_col] == "#":
                    print("no free space")
                    break
                
        for row in map_wh:
            print(row)
    
def load_csv(filename):
    map_wh = []
    controls = ""
    start_coord = ()
    with open(filename, "r") as file:
        reader = csv.reader(file)
        flag = False
        for row_i, row in enumerate(reader):
            if not row:
                flag = True
                continue
            if flag == False:
                map_wh.append(list(row[0]))
                for col_j, col in enumerate(row[0]):
                    if row[0][col_j] == "@":
                        start_coord = (row_i,col_j)
            else:
                controls += row[0] 
    return map_wh, controls, start_coord


if __name__ == "__main__":
    main()