
import math

def main():
    #input_string = "125 17"
    input_string = "6563348 67 395 0 6 4425 89567 739318"

    intial_stones = map(int, input_string.split())

    stone_count = {}
    for stone in intial_stones:
        stone_count[stone] = stone_count.get(stone, 0) +1 

    for i in range(75):
        print(f"Iteration: {i}")
        stone_count = apply_stone_rules(stone_count)
        total_stones = sum(stone_count.values())
        print(len(stone_count))


    print(f"Part 2: {total_stones}")

        
def apply_stone_rules(stone_count):

    new_count = {}

    for stone, count in stone_count.items():
        if stone == 0:
            new_count[1] = new_count.get(1, 0) + count
        elif len(str(stone)) % 2 == 0:
            left, right = split_number(stone)
            new_count[left] = new_count.get(left, 0) + count 
            new_count[right] = new_count.get(right, 0) + count 
        else:
            new_stone = stone*2024
            new_count[new_stone] = new_count.get(new_stone, 0) + count
   
    return new_count

def split_number(number: int):
    
    num_digits = len(str(number))
    divisor = 10 ** (num_digits // 2)
    
    first_half = number // divisor
    second_half = number % divisor
    
    return first_half, second_half


if __name__ == "__main__":
    main()