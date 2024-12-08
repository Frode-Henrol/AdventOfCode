import csv
from itertools import combinations

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
        col_index =0
    row_index = 0
        
                
# Generate all combinations of the coordinates
for key in stations:
    coordinates = stations[key]
    print(f"Key: {key}")
    print(coordinates)
    pairs = list(combinations(coordinates, 2))
    print("Pairs")
    print(pairs)
    # Find difference:
    differences = [(b[0] - a[0], b[1] - a[1]) for a, b in pairs]
    print("Differences:")
    print(differences)
    
    # 1. Tag par og find hvilket coord har mindst col værdi.
    # 2. Beregn afstand i col og i row.
    # 3. For coord med mindst col værdi træk afstand fra i col og row for coord.
    # 4. Går det samme for det andet coord i pair med højst col værdi, men bare læg afstand til.
    
    
    """
    for pair in pairs:
        print(f"pair: {pair[0][1]} and {pair[1][1]}")
        if pair[0][1] > pair[1][1]:
            difference = pair[0][1]-pair[1][1]
    """     


        

