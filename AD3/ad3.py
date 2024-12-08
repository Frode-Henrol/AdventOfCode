
# Load data
with open("ad3.txt", "r") as f:
    tot_string: str = ""
    for line in f:
        tot_string += line

# String to match
match1: str = "mul("

# Initilize values
valid_nums: list = []
parentes_inside_list: list = []
sum_total: int = 0
active = True

# Run through all indices in txt file
for i in range(len(tot_string)-8):
    
    # Deactivate if we hit dont
    if tot_string[i:i+7] == "don't()":
        active = False
        
    # Activate if we hit do
    elif tot_string[i:i+4] == "do()":
        active = True
    
    # If we hit a match and activation is true
    if active:
        if tot_string[i:i+4] == match1:

            # Run through chars after the match chars
            for j in range(8):
                
                # Make sure we are not indexing over max length
                if i+4+j < len(tot_string)-1:
                    
                    # Index until ")" is hit
                    if tot_string[i+4+j] == ")" and j <= 8:
                        
                        # Append the content inside "( )" to a list
                        parentes_inside_list.append(tot_string[i+4:i+4+j])

# This steps filters the last errors. Run through each contant in ( )
for inside in parentes_inside_list:
    comma_count = 0
    non_numcount = 0
    
    # Run through each char
    for char in inside:
        
        # Check if i contains comma
        if char == ",":
            comma_count+=1
            continue
        
        # Check if i contains not digits beside comma
        if not char.isdigit():
            non_numcount+=1
    
    # If i contains only 1 comma and digits append to valid nums list
    if non_numcount == 0 and comma_count == 1:
        valid_nums.append(inside)
        
# Loop over each number set and mulitply them and add to sum
for num in valid_nums:
    splitted_num = num.split(",")
    sum_total += int(splitted_num[0])*int(splitted_num[1])

    
print(sum_total)
    
        



    

        