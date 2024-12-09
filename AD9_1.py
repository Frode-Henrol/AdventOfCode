

def main():
    with open("ad9.txt", "r") as file:
        data = file.read()
        
    parsed_string = parse_data(data)
    #print(parsed_string)
    #print(len(parsed_string))

    digit_count = 0
    for char in parsed_string:
        if str(char).isdigit():
            digit_count+=1
    
    print(f"Digitcount: {digit_count}")

    all_string = []
    while True:
        
        shift_data(parsed_string)
        old = parsed_string[:]
        all_string.append(old)

        if len(all_string)>5 and all_string[-1] == all_string[-3]:
            break
        


    sum = calc_checksum(parsed_string, digit_count)
    print(sum)


    # parse string to new format
    
    
def calc_checksum(parsed_string, digit_count):
    sum = 0
    for i in range(digit_count):
        sum += int(parsed_string[i])*i
    return sum


def shift_data(parsed_string, show_print = False):

    for i in range(len(parsed_string)-1):
        # Check for "."
        
        if parsed_string[i] == ".":
            
            # Check the data from the right
            for j in range(1,len(parsed_string)):
                if parsed_string[-j] != ".":
                    
                    # Swap data and empty space
                    parsed_string[i], parsed_string[-j] = parsed_string[-j], parsed_string[i]
                    if show_print:
                        print(f"{parsed_string}")
                    return parsed_string
                    
    

def parse_data(data):
    
    parsed_data_string = []
    empty_space = False
    index_data = 0
    
    for num in range(len(data)):
        
        if empty_space == True:
            empty_space = False
            for _ in range(int(data[num])):
                parsed_data_string.append(".")
            
        elif empty_space == False:
            empty_space = True
            for _ in range(int(data[num])):
                parsed_data_string.append(index_data)
            index_data +=1
        
    return parsed_data_string
        
    
if __name__ == "__main__":
    main()