import csv


def main():
    char_main_list = []
    mas_count: int = 0
    
    # Open file in into matrix:
    with open("ad4.csv", "r") as file:
        reader = csv.reader(file)
        # For each row in csv
        for row in reader:
            # Create new list of chars and put into char_main_list forming a matrix of chars
            char_main_list.append([char for char in row[0]])

    # Length of matrix (square)
    length = len(char_main_list)
    
    # Run through the matrix row and col and creat 3x3 submatrices
    for row in range(length-2):      
        for col in range(length-2):
            subgrid = sub_grid(char_main_list, col, row)
            # Retrieve diagonals for subgrid
            diagonal_list = get_all_diagonal_lists(subgrid)
            # Chech for "MAS"
            mas_count+=check_for_mas(diagonal_list)
            
    print(mas_count)
#----------------------------------------------------
#-
#---------------------------------------------------- 
def sub_grid(matrix, start_col, start_row, size=3):
    return [row[start_col:start_col+size] for row in matrix[start_row:start_row+size]]
#----------------------------------------------------
#-
#---------------------------------------------------- 
def check_for_mas(inputlist):
    # Find the 2 longest sub_list i diagonal list:
    sorted_length = sorted(inputlist, key=len, reverse=True)[:2]

    mas_count_sub = 0
    
    # Check each diagonal for "MAS" and "SAM" and count +1 if both diagonal inlucde it
    for diagonal in sorted_length:
        row_string = "".join(diagonal)
        mas_count_sub += row_string.count("MAS") + row_string.count("SAM")
    if mas_count_sub == 2:
        return 1
    return 0
#----------------------------------------------------
#-
#---------------------------------------------------- 
def get_all_diagonal_lists(char_main_list):
    length = len(char_main_list)

    # Convert all rising diagonals to lists
    rising_diagonal1 = find_diagonal(char_main_list,length)

    # need to rotate and flip since find_diagonal function only can convert the upper-left half of the matrix
    flipped_main_list = [row[::-1] for row in char_main_list]
    flipped_main_list = flipped_main_list[::-1]
    rising_diagonal2 = find_diagonal(flipped_main_list,length-1)[::-1]

    # Repeats like before just for the falling diagonals
    flipped_main_list = [row[::-1] for row in char_main_list]
    falling_diagonal1 = find_diagonal(flipped_main_list,length)
    flipped_main_list = [row[::-1] for row in flipped_main_list]
    flipped_main_list = flipped_main_list[::-1]

    falling_diagonal2 = find_diagonal(flipped_main_list,length-1)[::-1]
    return rising_diagonal1+rising_diagonal2+falling_diagonal1+falling_diagonal2
#----------------------------------------------------
#-
#---------------------------------------------------- 
def find_diagonal(main_list,amount):
   col = 0
   row = 0
   diagonal_list =[]
   # Only works to the middlepoint of matrix...
   for startrow in range(amount):
       temp_list =[]
       while True:
           if row + startrow >= 0:
               char = main_list[row+startrow][col]
               temp_list.append(char)
               col+=1
               row-=1
           else:
               col=0
               row=0
               break
       diagonal_list.append(temp_list)
   return diagonal_list
#----------------------------------------------------
#-
#---------------------------------------------------- 

if __name__ == "__main__":
    main()