import csv

def main():
    
    rule_list = []
    order_list = []
    
    with open("ad5.csv", "r") as file:
            reader = csv.reader(file)
            # For each row in csv
            
            flag_orders = False
            
            for row in reader:
                
                if not row:
                    flag_orders = True
                # Create new list of chars and put into char_main_list forming a matrix of chars
                if flag_orders == False:
                    rule_list.append(row)
                else:
                    order_list.append(row)
                
    # Convert the rule list to more usefull format                         
    temp_rule_list = []
    # Split rules and put them into list
    for rule in rule_list:
        # Make sure rule is not empty
        if rule:
            temp_rule_list.append(rule[0].split("|"))
    rule_list = temp_rule_list

    # Sort for correct updates
    correct_updates, failed_updates, corrected_updates = return_updates(rule_list, order_list)
    
    # Find sum of middle value of correct:
    total_sum = middle_values_sum(correct_updates)

    #print(f"New order list: {failed_updates}")
    print(f"First part: {total_sum}")
    
    # New list to keep track of all the corrected fails:
    new_corrected = []
    
    # Runs this loop until all fails are corrected:
    while True:

        # Retrireve correct, fails and corrected lists of updates and input again the corrected to be check again
        correct_updates, failed_updates, corrected_updates = return_updates(rule_list, corrected_updates)
        
        # Since we input corrected_updates into the second arg in return_updates all the correct_updates returned most be correctly changed updates
        # We append these to the new_corrected list to keep track of all the corrected updates
        if correct_updates:
            for update in correct_updates:
                if update not in new_corrected:
                    new_corrected.append(update)
        
        # When we don't receive any fail we break the loop, since all the failed updates has been corrected
        if not failed_updates:
            break
    
    # Find sum of middle value fails but now corrected:
    total_sum = middle_values_sum(new_corrected)
    print(f"Second part: {total_sum}") 
#----------------------------------------------------
#-
#---------------------------------------------------- 
def return_updates(rule_list, order_list):
    accepted_updates = []
    failed_updates = []
    corrected_updates = []
    
    # For each update
    for update in order_list:
        #print(f"\nWe are looking at the update: {update}")
        # For each number in an update, like: "75",47,61,53,29
        for num in update:
            
            # Next we check all the rules if the num is in the first index, like: "75"|29
            for rule in rule_list:
                
                # If the num is in the first index in rule:
                if num == rule[0]:
                    
                    # Check all the other names in the update_list
                    for num2 in update:
                        
                        # Make sure we do not check the current num
                        if num != num2:
                            
                            # Check for rules which starts with num and end with number in update, like: "75" | number in update (that is not 75)
                            if rule[1] == num2:
                                
                                # Find index of the number we are checking for
                                num_index = update.index(num)
                                
                                # Find index of the other number found i rule
                                num_second_index = update.index(num2)
                                
                                # If our numbers index is less than the second index in the rule do nothing, if bigger the update is a fail.
                                if num_index < num_second_index:
                                    #print(f"Num: {num} has smaller index than {num2}")
                                    pass
                                # If our number does not follow the rules i has applied it is a failed update
                                else:
                                    #print(f"Num: {num} has bigger index than {num2}")
                                    
                                    # Add the fail to failed list if it is not already in the list
                                    if update not in failed_updates:
                                        failed_updates.append(update)
                                    
                                    # For part 2 we just take the value that 
                                    update[num_index], update[num_second_index] = update[num_second_index], update[num_index] 
                                    
                                    if update not in corrected_updates:
                                        corrected_updates.append(update)
                                        
    # Lastly only return non failure updates and non empty updates               
    for update in order_list:
        if update not in failed_updates and update:
            accepted_updates.append(update)
    
                                
    return accepted_updates, failed_updates, corrected_updates
#----------------------------------------------------
#-
#----------------------------------------------------                  
def middle_values_sum(list_of_lists):
    sum=0
    for sub_list in list_of_lists:
        middle_index = len(sub_list)//2
        sum += int(sub_list[middle_index])
    return sum
#----------------------------------------------------
#-
#----------------------------------------------------  
if __name__ == "__main__":
    main()