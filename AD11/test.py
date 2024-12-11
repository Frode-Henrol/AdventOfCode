

def main():
    input_string = "6563348 67 395 0 6 4425 89567 739318"
    initial_stones = map(int, input_string.split())
    
    stone_counts = {}
    for stone in initial_stones:
        stone_counts[stone] = stone_counts.get(stone, 0) + 1
    
    for _ in range(75):
        stone_counts = process_stones(stone_counts)
        total_stones = sum(stone_counts.values())
        print(f"Total stones after blink: {total_stones}")

def process_stones(stone_counts):
    new_counts = {}
    for stone, count in stone_counts.items():
        if stone == 0:
            new_counts[1] = new_counts.get(1, 0) + count
        elif len(str(stone)) % 2 == 0:
            left, right = split_number(stone)
            new_counts[left] = new_counts.get(left, 0) + count
            new_counts[right] = new_counts.get(right, 0) + count
        else:
            new_stone = stone * 2024
            new_counts[new_stone] = new_counts.get(new_stone, 0) + count
    return new_counts

def split_number(number):
    num_digits = len(str(number))
    divisor = 10 ** (num_digits // 2)
    return number // divisor, number % divisor

if __name__ == "__main__":
    main()
