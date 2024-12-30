def main():
    filename = "ad19.txt"
    with open(filename) as f:
        data = f.read().split("\n")
    
    towel_flag = False
    towel_choices = []
    towel_designs = []

    # Split towel choices and towel designs into separate lists
    for row in data:
        if row == "":
            towel_flag = True
            continue
        if towel_flag:
            towel_designs.append(row)
        else:
            towel_choices = [choice.strip() for choice in row.split(",")]

    print("Towel Choices:", towel_choices)
    print("Towel Designs:", towel_designs)

    # Use recursion to count the number of ways each towel design can be made
    total_ways = 0
    total_valid_towels = 0
    memo = {}
    for towel_design in towel_designs:
        ways = count_design_ways(towel_design, towel_choices, memo)
        total_ways += ways

        if ways != 0:
            total_valid_towels += 1

    print(f"Part 1: {total_valid_towels}")
    print(f"Part 2: {total_ways}")

def count_design_ways(towel_design, towel_choices, memo):
    # If the design is in the memo, return its stored value
    if towel_design in memo:
        return memo[towel_design]

    # Base case: an empty design has 1 way (do nothing)
    if not towel_design:
        memo[towel_design] = 1
        return 1

    total_ways = 0

    # Try every possible prefix of the design
    for choice in towel_choices:
        if towel_design.startswith(choice):
            remaining_design = towel_design[len(choice):]
            total_ways += count_design_ways(remaining_design, towel_choices, memo)

    # Store the result in the memo
    memo[towel_design] = total_ways
    return total_ways

if __name__ == "__main__":
    main()
