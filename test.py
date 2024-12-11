import math

def get_digit_length(number: int):
    if number == 0:
        return 1
    return math.floor(math.log10(abs(number))) + 1

def split_number(number: int):
    
    num_digits = get_digit_length(number)
    divisor = 10 ** (num_digits // 2)
    
    first_half = number // divisor
    second_half = number % divisor
    
    return first_half, second_half

number = 1000

print(split_number(number))