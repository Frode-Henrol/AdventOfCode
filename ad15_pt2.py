import csv


def main():

    filename = "test1.csv"
    map_wh, controls, start_coord = load_csv(filename)
    for row in map_wh:
        print(row)
        
    print(controls)
    print(start_coord)
    
    execute_controls(controls, map_wh, start_coord)
    
    sum_box = calculate(map_wh)

    print(sum_box)

    for row in map_wh:
        print(row)
        

def calculate(map_wh):
    sum_box = 0
    for row_i, row in enumerate(map_wh):
        for col_i, col in enumerate(row):
            if map_wh[row_i][col_i] == "O":
                sum_box += row_i * 100 + col_i
    return sum_box

def execute_controls(controls, map_wh: list, start_coord):
    coord = start_coord
    print(f"Start coord: ({start_coord})")
    # Run through each control in string
    for control in controls:
        print(f"Control used: {control}")
        move_str = ""
        if control == "^":
            move = (-1, 0)
            move_str = "up"
        elif control == "v":
            move = (1, 0)
            move_str = "down"
        elif control == "<":
            move = (0, -1)
            move_str = "left"
        elif control == ">":
            move = (0, 1)
            move_str = "right"
        
        # Update move coordinat
        coord_row, coord_col = coord
        move_row, move_col = move
        new_row, new_col = coord_row + move_row, coord_col + move_col

        # Check for empty space or box, do nothing if wall
        next_tile = map_wh[new_row][new_col]
        print(f"NEXT TILE: ({next_tile})")
        if next_tile == ".":
            print("Free space")
            coord = new_row, new_col
            map_wh[coord_row][coord_col] = map_wh[new_row][new_col]  
            map_wh[new_row][new_col] = "@"
            
        
        elif next_tile == "[" or next_tile == "]":
            if move_str == "left" or move_str == "right":
                iter = 0
                while True:
                    iter += 1
                    new_row, new_col = coord_row + move_row, coord_col + move_col # For @
                    newnew_row, newnew_col = coord_row + move_row * iter, coord_col + move_col * iter
                    
                    if map_wh[newnew_row][newnew_col] == ".":
                        map_wh[newnew_row].pop(newnew_col)
                        map_wh[coord_row].insert(coord_col,".")
                        coord = new_row, new_col
                        break
    
                    elif map_wh[newnew_row][newnew_col] == "#":
                        print("no free space")
                        break
                    
            if move_str in ["up", "down"]:
                
                # MANGLER SMART MØDE AT TJEKKE FOR boks over 
                
                
                # 1. Hvis current tile er [ tjek højre, hvis ] tjek venstre
                    # (For hver) Hvis current tile != next tile -> gå til 1. ellers gå til next tile.
                        # Hvis next tile = # break
                
                pass     
                
        for row in map_wh:
            print(row)

def check(map_wh, new_row , new_col):
    if map_wh[new_row][new_col] == "[":
        pass
    elif map_wh[new_row][new_col] == "]":
        pass



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
            else:
                controls += row[0] 
    for row in map_wh:
        print(row)
        
    map_wh_pt2 = []
    for row_i, row in enumerate(map_wh):
        new_row = []
        for col_i, col in enumerate(row):
            if col == "#":
                new_row.append("#")
                new_row.append("#")
            elif col == ".":
                new_row.append(".")
                new_row.append(".")
            elif col == "O":
                new_row.append("[")
                new_row.append("]")
            elif col == "@":
                new_row.append("@")
                new_row.append(".")
                

        map_wh_pt2.append(new_row)
        
    for row_i, row in enumerate(map_wh_pt2):
        new_row = []
        for col_i, col in enumerate(row):
            if row[col_i] == "@":
                start_coord = (row_i,col_i)
                
    return map_wh_pt2, controls, start_coord

class Box:
    def __init__(self, coord):
        self.coord = coord
        
    def update_coord(self, new_coord):
        self.coord = new_coord
        

if __name__ == "__main__":
    main()