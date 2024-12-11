
import math

def main():
    #input_string = "125 17"
    input_string = "6563348 67 395 0 6 4425 89567 739318"

    stone_list_string = input_string.split()
    stone_list = []
    
    print(stone_list_string)
    for stone in stone_list_string:
        stone_list.append(int(stone))
        
    print(stone_list)

    for i in range(75):
        print(f"Iteration: {i}")
        #stone_list_string = apply_stone_rules_part1(stone_list_string)
        stone_list = apply_stone_rules_part2(stone_list)
        #print(stone_list)
    
    print(f"Part 1: {len(stone_list)}")


def apply_stone_rules_part1(stone_list_string):
    new_stone_list_string: list = []
    
    for i in range(len(stone_list_string)):
        stone = stone_list_string[i]
        #print(f"Stone num: {stone} Stone index: {stone_index}")
        
        # If 0 make it 1
        if int(stone) == 0:
            
            new_stone_list_string.append("1")

        # If even split
        elif len(stone) % 2 == 0:
            stone_left, stone_right = stone[:len(stone)//2], stone[len(stone)//2:]
            
            # If right is pure zeros make it a single 0
            if stone_right.strip("0") == "":
                stone_right ="0"
                #print(f"Pure zeros: {stone_right}")
            else:
                # Else remove only leading zeroes
                stone_right = stone_right.lstrip("0")
                
            new_stone_list_string.append(stone_left)
            new_stone_list_string.append(stone_right)
        else:
            new_stone_list_string.append(str(int(stone)*2024))
            
    return new_stone_list_string
        
def apply_stone_rules_part2(stone_list):
    new_stone_list: list = []
    
    for i in range(len(stone_list)):
        stone: int = stone_list[i]
        #print(f"Stone: {stone}")

        if stone == 0:
            new_stone_list.append(1)

        elif len(str(stone)) % 2 == 0:
            stone_left, stone_right = split_number(stone)
                
            new_stone_list.append(stone_left)
            new_stone_list.append(stone_right)
        else:
            new_stone_list.append(stone*2024)
            
    return new_stone_list

def split_number(number: int):
    
    num_digits = len(str(number))
    divisor = 10 ** (num_digits // 2)
    
    first_half = number // divisor
    second_half = number % divisor
    
    return first_half, second_half


if __name__ == "__main__":
    main()