

def main():
    with open("ad9.txt", "r") as file:
        data = file.read()
        
    parsed_string_list, data_count = parse_data(data)
    #print(len(parsed_string))
    #print_2(parsed_string_list)
    
    # parse
    parsed_string_list, all_moves = shift_data(parsed_string_list, data_count)
    
    """
    for i in range(len(all_moves)):
        print_test= print_2(all_moves[-i])
        print(calc_checksum(print_test))
    """ 
        

    
def calc_checksum(parsed_string):
    sum = 0
    for i in range(len(parsed_string)):
        if parsed_string[i] != ".":
            sum += int(parsed_string[i])*i
    return sum


def shift_data(data, data_count):
    data_2 = data[:]
    flag = False
    
    all_moves = []
    
    #print(f"Data2 {data_2}")
    
    for num_for_check in range(data_count):
        index = data_count - num_for_check 
        #print(index-1)
        for right_i in range(1,len(data)):
            
            # If data is found
            #print(f"From right: {data[-right_i]} and index is: {index}")
            if data[-right_i][0] == index:
                #print(f"Data: {data[-right_i]}")
                
                for left_i in range(len(data) - right_i):
                    #print(f"From left: {data[left_i]}")
                    # If empty space is found and the empty space is bigger or smaller than the data
                    if data[left_i][0] == 0 and data[left_i][1] >= data[-right_i][1]:
                        #print(index)
                        #print(f"Empty space: {data[left_i]}, {data[left_i][1]} free spaces for {data[-right_i][1]} data")
                        
                        #data[left_i], data[-right_i] = data[-right_i], data[left_i]
                        diff = data[left_i][1]-data[-right_i][1]
                        if diff != 0:
                            data.insert(left_i+1,(0,diff))
                        
                        data[left_i] = data[-right_i]
                        
                        
                        data.insert(-right_i,(0,data[-right_i][1]))
                        data.pop(-right_i)

                        all_moves.append(data)
                        flag = True
                        break
                        
                if flag:
                    break
        if index < 4300:
            print_test= print_2(data)
            print(f"{calc_checksum(print_test)} index: {index}")
        else:
            if index%100==0:
                print_test= print_2(data)
                print(f"{calc_checksum(print_test)} index: {index}")
                
    return data_2, all_moves      
        
def print_2(data_list):
    string_tot = []
    for data in data_list:
        if data[0] != 0:
            for num in range(data[1]):
                string_tot.append(str(data[0]-1))
        else:
            for num in range(data[1]):
                string_tot.append(".")
    #print("".join(string_tot))
    return "".join(string_tot)

def parse_data(data):
        
    data_block = []
    
    data_indexing = 1
    for i in range(len(data)):
        
        if i%2==0:
            data_block.append((int(data_indexing),int(data[i])))
            data_indexing+=1
        else:
            data_block.append((0,int(data[i])))

    print(f"Parsed data block: {data_block}")
    return data_block, data_indexing


if __name__ == "__main__":
    main()