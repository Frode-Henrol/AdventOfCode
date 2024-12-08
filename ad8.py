import csv


stations = {}


# Opens and sort each station into dic where key is name like "A" and value is a list of tuples of the row, col index
with open("ad8.csv", "r") as file:
    reader = csv.reader(file)

    row_index = 0
    col_index = 0

    for row in reader:
        row_index+=1
        for col in row[0]:
            col_index+=1
            if col != ".":
                if col not in stations:
                    stations[col] = []
                stations[col].append((row_index, col_index))
                

for key in stations:
    print(key)


