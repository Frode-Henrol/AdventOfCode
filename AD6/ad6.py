import csv

def main():
    
    # PART 1 ---------------------------------------------------
    
    # Made is made
    filename = "ad6.csv"
    gameboard = load_map(filename)
    print(f"y len: {len(gameboard)} x len: {len(gameboard[0])}")
    
    # Run game
    guard = run_guard(gameboard)
    print_map(gameboard, guard)
   
    # Get total uniq steps
    total_steps = len(list(set(guard.get_position_list())))
    print(f"Total steps: {total_steps}")
    
    print(guard.objects_hit)
    
    # PART 2 ---------------------------------------------------
    
    loop_count = 0
    gameboard = load_map(filename)
    runs_checked = 0
    
    # Go through map and place # at each empty space and run the guard sequence
    for y_coord in range(len(gameboard)):
        for x_coord in range(len(gameboard)):
           
            print(f"Runs checked: {runs_checked} out of somewhere under {130*130}")
            # Make a deep copy of the gameboard
            gameboard_test = [row.copy() for row in gameboard]

            # Place # if empty (.) otherwise skip
            if gameboard_test[y_coord][x_coord] == "#" or gameboard_test[y_coord][x_coord] == "^":
                continue
            gameboard_test[y_coord][x_coord] = "#"
            
            # Run the guard
            guard = run_guard(gameboard_test)
            
            # If stuck in loop add to counter
            if guard.in_loop:
                print_map(gameboard_test, guard)
                loop_count +=1

            runs_checked +=1
            
    print(f"Loop count: {loop_count}")
#----------------------------------------------------
#-
#---------------------------------------------------- 
def run_guard(gameboard):
    
    # Creat guard instance
    guard = Guard(gameboard)
    
    # Run loop of guard moving:
    while True:

        # Break if out of bounds or loop is reached
        if guard.out_of_bounds or guard.in_loop:  
            #print(f"OUT OF BOUNDS? {guard.out_of_bounds} IN A LOOP? {guard.in_loop}")
            break
        
        # Move the guard forward
        guard.move()
        
    return guard
#----------------------------------------------------
#-
#---------------------------------------------------- 
def load_map(filename):
    game_board =[]
    with open(filename, "r") as file:
        reader = csv.reader(file)
        
        for row in reader:
            game_board.append(list(row[0]))
    
    return game_board
#----------------------------------------------------
#-
#---------------------------------------------------- 
def print_map(gameboard, guard):
    # Paint path wtih "X"
    for coord in guard.get_position_list():
        y, x = coord
        gameboard[y][x] = "X"
    
    # Print map
    for row in gameboard:
        print("".join(row))
#----------------------------------------------------
#-
#---------------------------------------------------- 
class Guard:
    directions = {
        "up": (-1, 0),
        "right": (0, 1),
        "down": (1, 0),
        "left": (0, -1),
    }
     
    def __init__(self, gameboard: list, start_direction: str = "up"):
         self.position: list = self.start_pos(gameboard)
         self.position_list: list = []
         self.objects_hit = []
         
         self.direction = start_direction
         self.gameboard = gameboard
         
         self.coords_crossed = []
         
         self.out_of_bounds = False
         self.in_loop = False
#----------------------------------------------------
#-
#----------------------------------------------------  
    def start_pos(self, game_board):
        for row_index, row in enumerate(game_board):
            for col_index, value in enumerate(row):
                if value == "^":
                    #print((row_index, col_index))
                    return (row_index, col_index)
#----------------------------------------------------
#-
#---------------------------------------------------- 
    def move(self):
        # Current coords:
        y, x = (self.position)
        dir_y, dir_x = self.directions[self.direction]
        #print(f"Pos: y: {y} x: {x}") ---------------------!
        # Next move coordinats
        next_move = (y+dir_y, x+dir_x)
       
        # Check for loop
        self.detect_loop()
        
        # Check for edge 
        if not self.detect_edge(next_move):
            
            # Check for object
            if self.detect_object(next_move):
                self.turn_right()

            else:
                # Update player coordinate
                self.position = next_move
                self.position_list.append(self.position)
#----------------------------------------------------
#-
#----------------------------------------------------   
    def detect_object(self, next_move):
        y, x = next_move
        if self.gameboard[y][x] == "#":        
            self.objects_hit.append([self.direction,next_move])
            return True
        return False
#----------------------------------------------------
#-
#---------------------------------------------------- 
    def detect_edge(self, next_move):
        y, x = next_move
        if y > len(self.gameboard)-1 or y<0 or x > len(self.gameboard[0])-1 or x<0:
            self.out_of_bounds = True
            return True
        return False
#----------------------------------------------------
#-
#----------------------------------------------------  
    def turn_right(self):
        direction_map = {
            "up": "right",
            "right": "down",
            "down": "left",
            "left": "up"
        }
        self.direction = direction_map[self.direction]
#----------------------------------------------------
#-
#---------------------------------------------------- 
    def detect_loop(self):
        unique_items = set()

        # Iterate through the list
        for item in self.objects_hit:
            if tuple(item) in unique_items:
                self.in_loop = True
            else:
                # Add the item to the set for future comparison
                unique_items.add(tuple(item))
#----------------------------------------------------
#-
#---------------------------------------------------- 
    def get_position_list(self):
        return self.position_list




if __name__ == "__main__":
    main()