import csv


def main():

    filename = "ad15.csv"
    map_wh, controls, start_coord = load_csv(filename)
    for row in map_wh:
        print(row)
        
    print(controls)
    print(start_coord)
    
    execute_controls(controls, map_wh, start_coord)
    
    sum_box = calculate(map_wh)

    print(sum_box)

    #for row in map_wh:
    #    print(row)
        
def calculate(map_wh):
    sum_box = 0
    for row_i, row in enumerate(map_wh):
        for col_i, col in enumerate(row):
            if map_wh[row_i][col_i] == "[":
                sum_box += row_i * 100 + col_i
    return sum_box

def execute_controls(controls, map_wh: list, start_coord):
    coord = start_coord
    print(f"Start coord: ({start_coord})")
    # Run through each control in string
    for control in controls:
        #print(f"Control used: {control}")
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
        new_coord = new_row, new_col
    
        walls = set()
        free_space = set()
        boxes = {}

        # Check for empty space or box, do nothing if wall
        next_tile = map_wh[new_row][new_col]
        #print(f"NEXT TILE: ({next_tile})")
        if next_tile == ".":
            #print("Free space")
            coord = new_row, new_col
            map_wh[coord_row][coord_col] = map_wh[new_row][new_col]  
            map_wh[new_row][new_col] = "@"
            
        elif next_tile in "[]":
            if move_str in ["up","down"]:
                # Check for walls or free space
                walls, free_space, boxes = check_up_down(move, new_coord, map_wh, walls, free_space, boxes)
                if not walls:
                    for coord in boxes:
                        row, col = coord
                        map_wh[row][col] = "."
                    for coord in boxes:
                        row, col = coord
                        map_wh[row+move[0]][col] = boxes[coord]
                    map_wh[coord_row][coord_col] = "." 
                    map_wh[new_row][new_col] = "@"
            
            if move_str in ["left","right"]:
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
                        #print("no free space")
                        break

def check(map_wh, new_row , new_col):
    if map_wh[new_row][new_col] == "[":
        pass
    elif map_wh[new_row][new_col] == "]":
        pass

def check_up_down(move: tuple, new_coord: tuple, map_wh: list, walls: set, free_space: set, boxes: set):

    coord_row, coord_col = new_coord # Coord to check
    move_row, move_col = move        # Amount to move
    next_row, next_col = coord_row + move_row, coord_col + move_col   # Next coord.
    new_coord = next_row, next_col    # Next coord again to check for symbol
    current_tile = map_wh[coord_row][coord_col]
    #print(f"Current tile: {current_tile} ({coord_row},{coord_col})")

    if current_tile == "#":
        walls.add((coord_row, coord_col))
        return walls, free_space, boxes
    
    if current_tile == ".":
        free_space.add((coord_row, coord_col))
        return walls, free_space, boxes
    
    # Makes sure the offset is correct based on what bracket were look at.
    if current_tile == "[":
        dir = 1    
    elif current_tile == "]":
        dir = -1

    walls, free_space, boxes = check_up_down(move, (next_row,next_col), map_wh, walls, free_space, boxes)
    walls, free_space, boxes = check_up_down(move, (next_row,next_col+dir), map_wh, walls, free_space, boxes)
    
    if map_wh[coord_row][coord_col+dir] in "[]":
        boxes[(coord_row, coord_col+dir)] = map_wh[coord_row][coord_col+dir]
    boxes[(coord_row, coord_col)] = map_wh[coord_row][coord_col]
    
    return walls, free_space, boxes

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

if __name__ == "__main__":
    main()