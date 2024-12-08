

import csv

sum = 0

with open("test.csv","r") as f:
    reader = csv.reader(f, delimiter=' ')
    
    for report in reader:
                    
        up_count = 0
        down_count = 0
        fail_count = 0
        
        false_report = False
        
        for sub_report_index in range(len(report)-1):
            sub_report = report[:]
            del sub_report[sub_report_index]
            print(sub_report)
            
            for index in range(len(sub_report)-1):

                current_index = int(sub_report[index])
                next_index = int(sub_report[index+1])
                #print(f"Current index: {current_index} Next index: {next_index}")
                
                if next_index > current_index:
                    up_count +=1
                    
                if next_index < current_index:
                    down_count +=1
                
                if (up_count > 2 and down_count > 1) or (up_count > 1 and down_count > 2):
                    false_report = True
                
                difference = abs(next_index - current_index)
                
                if difference > 3 or difference == 0:
                    false_report = True
                
            
            if false_report:
                print(f"Report: {sub_report} Upcount: {up_count} Downcount: {down_count} FALSE")  
                continue
            print(f"Report: {sub_report} Upcount: {up_count} Downcount: {down_count} TRUE")  
            
            sum+=1

print(sum)