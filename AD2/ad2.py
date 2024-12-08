

import csv


def main():
    sum = 0
    with open("ad2.csv","r") as f:
        reader = csv.reader(f, delimiter=' ')
        
        # Check each report
        for report in reader:
            
            # Find the fail count
            fail_count = fail_counter(report)
            
            # If failcount over 0 then try removing numbers from report
            if fail_count > 0:
                print(f"Report: {report} need to be revised")
                for sub_report_index in range(len(report)):
                    fail_count_sub = 0
                    # Copy the report in a new list
                    sub_report = report[:]
                    # Remove value at index
                    del sub_report[sub_report_index]
                    
                    # Find the failcount
                    fail_count_sub = fail_counter(sub_report)
                    
                    print(f"Failcount for sub report: {sub_report} is {fail_count_sub}")
                    
                    # If we find a report configuration that gives 0 fails -> break
                    if fail_count_sub == 0:
                        sum+=1
                        break
            else:
                sum+=1
    print(f"The sum is: {sum}")


def fail_counter(report):
    up_count = False
    down_count = False
    fail_count = 0
    
    # Loop through each number in report
    for index in range(len(report)-1):
        
        current_index = int(report[index])
        next_index = int(report[index+1])
        
        # Detect increase
        if next_index > current_index:
            up_count = True
        # Detect decrease 
        if next_index < current_index:
            down_count = True
            
        # Log fail if there is decrease and increase
        if up_count and down_count:
            fail_count +=1
            up_count = False
            down_count = False
         

        difference = abs(next_index - current_index)
        
        # Check if difference is within tolerence   
        if difference > 3 or difference == 0:
            fail_count +=1
        
    return fail_count


if __name__ == "__main__":
    main()