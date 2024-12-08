import csv


def main():
   char_main_list = []
   xmas_count: int = 0
   # Open file in into matrix:
   with open("ad4.csv", "r") as file:
       reader = csv.reader(file)
       # For each row in csv
       for row in reader:
           # Create new list of chars and put into char_main_list forming a matrix of chars
           char_main_list.append([char for char in row[0]])
           
   # Find for horizontal:
   xmas_count += check_for_xmas(char_main_list)
   print(xmas_count)
   
   # Rotate to find vertical
   rotated_char_main_list = rotate_90(char_main_list)
   xmas_count+=check_for_xmas(rotated_char_main_list)
   print(xmas_count)
   
   #Find diagonals:
   diagonals_char_main_list = get_all_diagonal_lists(char_main_list)
   
   for list in diagonals_char_main_list:
       print(list)
   #print(diagonals_char_main_list)
   xmas_count+=check_for_xmas(diagonals_char_main_list)
   print(xmas_count)
#----------------------------------------------------
#-
#---------------------------------------------------- 
def check_for_xmas(char_main_list):
   sub_xmas_count = 0
   for char_list in char_main_list:
       row_string = "".join(char_list)
       sub_xmas_count += row_string.count("XMAS") + row_string.count("SAMX")
   return sub_xmas_count
#----------------------------------------------------
#-
#---------------------------------------------------- 
def rotate_90(char_main_list):
   
   # Kan bare brug [::-1] istedet
   rotated_list_of_lists = []
   
   # Length of row and col
   row_length = len(char_main_list)
   col_length = len(char_main_list[0])
   
   # Go through col and row
   for col_index in range(col_length):
       new_row = []
       for row_index in range(row_length):
           
           # Append new row (old col) to rotated list of lists.
           new_row.append(char_main_list[row_index][col_index])
       rotated_list_of_lists.append(new_row)    
   return rotated_list_of_lists
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