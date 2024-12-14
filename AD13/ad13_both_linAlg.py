import csv

def main():
    filename = "ad13.csv"
    clawmachine_data_total = process_csv(filename)
    print(f"Claw machines in total: {len(clawmachine_data_total)}")

    # Part 1 calculation
    total_cost = 0
    for clawmachine_data in clawmachine_data_total:
        total_cost += solve_equation(clawmachine_data, False)
    print(f"Part 1: {total_cost}")
    
    # Part 2 calculation
    total_cost = 0
    for clawmachine_data in clawmachine_data_total:
        total_cost += solve_equation(clawmachine_data, True)
    print(f"Part 2: {total_cost}")


def solve_equation(clawmachine_data, pt):
    # Data
    button_A = clawmachine_data[0]
    button_B = clawmachine_data[1]
    goal = clawmachine_data[2]

    # Parse values
    a_x, a_y = map(int, button_A)
    b_x, b_y = map(int, button_B)
    goal_x, goal_y = map(int, goal)
    
    if pt:
        goal_x += 10000000000000
        goal_y += 10000000000000

    # Determinant 
    det_A = a_x * b_y - b_x * a_y  

    if det_A == 0:
        # If determinant = 0 (linearly dependent equations)
        n1 = goal_x // a_x  # Check how many times to press A
        n2 = goal_x // b_x  # Check how many times to press B

        # If A's solution works and is better than B's, return the cost for A
        if [n1 * a_x, n1 * a_y] == [goal_x, goal_y] and 3 * n1 < n2:
            return 3 * n1
        elif [n2 * b_x, n2 * b_y] == [goal_x, goal_y]:
            return n2
        else:
            return 0
    else:
        # If the determinant is not zero, we can solve the system
        det_B_x = goal_x * b_y - goal_y * b_x
        det_B_y = a_x * goal_y - a_y * goal_x

        # Check if the results are integers and satisfy the equations
        x = det_B_x // det_A
        y = det_B_y // det_A

        if det_B_x % det_A == 0 and det_B_y % det_A == 0:  # Ensure both divisions are exact
            return 3 * x + y
        else:
            return 0


def process_csv(filename):
    grouped_data = []
    current_group = []

    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if not row:  # Skip empty rows
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
