import csv
import math

import itertools
 

def main():
    filename = "ad7.csv"
    
    data = load_file(filename)
    #print(data)
    
    correct_equa, goal_sum = solve(data)

    print(goal_sum)
    
    
def permutations(list_of_numbers):
    characters = ['*', '+','||']
    length = len(list_of_numbers) - 1

    # Generate all permutations
    permutations = list(itertools.product(characters, repeat=length))

    return permutations

def load_file(filename):
    data = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        
        for row in reader:
            splitted_string_main = row[0].split(":")
            splitted_string_sub = splitted_string_main[1].split(" ")[1:]
            splitted_string_sub = [int(num) for num in splitted_string_sub]
            
            data.append([int(splitted_string_main[0]),splitted_string_sub])
            #print([int(splitted_string_main[0]),splitted_string_sub])
    return data


def solve(data):
    
    correct_equa = []
    goal_sum = 0
    
    for equa in data:
        #print(f"We check: {equa}")
        goal = equa[0]
        numbers = equa[1]
        
        if goal == sum(numbers) or goal == math.prod(numbers):
            correct_equa.append(equa)
            goal_sum+=goal
            continue
        if brute_force(numbers, goal):
            correct_equa.append(equa)
            goal_sum+=goal
            continue

        #print(f"goal_sum {goal_sum}")


    return correct_equa, goal_sum
        

def brute_force(numbers, goal):
    # List for all equation perms
    permutation_list = permutations(numbers)

    # For each comb of + and * save to equations
    for perm in permutation_list:
        sub_equation = []
        
        for num_index in range(len(numbers)-1):
            sub_equation.append(str(numbers[num_index]))
            sub_equation.append(perm[num_index])
        sub_equation.append(str(numbers[len(numbers) - 1]))
        
        # skal lige lave 
        combined = "".join(sub_equation)
        #print(f"Goal: {goal} and the equa gives: {eval_left_to_right(numbers, perm)} and {combined}")

        if goal == eval_left_to_right(numbers, perm):
            #print(f"{combined} is = {goal}")
            
            return True
    return False



def eval_left_to_right(numbers, perm):
    # Split the expression into tokens (numbers and operators)
    #print(numbers)
    #print(perm)

    sum_perm = int(numbers[0])

    for i in range(len(perm)):  
        if perm[i] == "*":
            sum_perm = sum_perm * int(numbers[i+1])
            
        elif perm[i] == "+":
            sum_perm = sum_perm + int(numbers[i+1])

        elif perm[i] == "||":
            sum_perm = int(str(sum_perm)+str(numbers[i+1]))


    return sum_perm



if __name__ == "__main__":
    main()