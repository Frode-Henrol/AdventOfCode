import csv

def main():
    filename = "ad13.csv"
    clawmachine_data_total = process_csv(filename)
    print(f"Claw machines in total: {len(clawmachine_data_total)}")
    total_cost = 0
    for clawmachine_data in clawmachine_data_total:
        cost = check_claw_machine(clawmachine_data)
        if cost > 0:
            total_cost += cost
    print(f"Part 1: {total_cost}")

def check_claw_machine(clawmachine_data):
    # Data
    button_A = clawmachine_data[0]
    button_B = clawmachine_data[1]
    goal = clawmachine_data[2]

    # Parse values
    a_x, a_y = map(int, button_A)
    b_x, b_y = map(int, button_B)
    goal_x, goal_y = map(int, goal)

    # Constraints
    max_moves = 100
    cost_a, cost_b = 3, 1
    min_cost = float("inf")

    # Check combinations of button presses
    for press_A in range(max_moves + 1):
        for press_B in range(max_moves + 1):
            sum_x = press_A * a_x + press_B * b_x
            sum_y = press_A * a_y + press_B * b_y

            if sum_x == goal_x and sum_y == goal_y:
                cost = press_A * cost_a + press_B * cost_b
                min_cost = min(min_cost, cost)
                print(press_A,press_B)

    return min_cost if min_cost != float("inf") else 0


def process_csv(filename):
    grouped_data = []
    current_group = []

    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            # Skip empty rows
            if not row:
                continue

            # Extract digits and negative signs from the row
            extracted_row = [
                ''.join(char for char in entry if char.isdigit() or char == '-') for entry in row
            ]
            current_group.append(extracted_row)

            # Group rows in sets of 3
            if len(current_group) == 3:
                grouped_data.append(current_group)
                current_group = []

    return grouped_data

if __name__ == "__main__":
    main()
