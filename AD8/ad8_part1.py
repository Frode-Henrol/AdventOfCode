import csv
from itertools import combinations

stations = {}
map = []

# Opens and sort each station into dic where key is name like "A" and value is a list of tuples of the row, col index
with open("ad8.csv", "r") as file:
    reader = csv.reader(file)

    row_index = 0
    col_index = 0

    for row in reader:
        map.append(list(row[0]))
        
        for col in row[0]:
            if col != ".":
                if col not in stations:
                    stations[col] = []
                stations[col].append((row_index, col_index))
            col_index+=1
        row_index+=1
        col_index =0
    row_index = 0
        
print(map[2][8])

# Generate all combinations of the coordinates
for key in stations:
    coordinates = stations[key]
    print(f"Key: {key}")
    print(coordinates)
    pairs = list(combinations(coordinates, 2))
    print("Pairs")
    print(pairs)
    
    # 1. Tag par og find hvilket coord har mindst col værdi.
    for pair in pairs:
        print(f"Pair: {pair}")
    
        if pair[0][1] > pair[1][1]:
            pair_min = pair[1]
            pair_max =  pair[0]
        else:
            pair_min = pair[0]
            pair_max = pair[1]
        
        print(f"Pair min: {pair_min} Pair max: {pair_max}")
        
        """
        # Skal slettes - - - -
        row, col = pair_min
        print(f"minprint: {row} {col} and {map[row][col]}")
        map[row][col] = "min"
        
        row, col = pair_max
        print(f"maxprint: {row} {col}")
        map[row][col] = "max"
        # Skal slettes - - - -
        """
        
        # 2. Beregn afstand i col og i row.
        diff = tuple(a - b for a, b in zip(pair_max, pair_min))
        print(f"Difference: {diff}")
        
        # 3. For coord med mindst col værdi træk afstand fra i col og row for coord.
        sub_antenne = []
        sub_antenne.append(tuple(a - b for a, b in zip(pair_min, diff)))
        sub_antenne.append(tuple(a + b for a, b in zip(pair_max, diff)))

        # 4. For visuelt debug print antinode på map
        for sub in sub_antenne:
            print(f"Sub antenne: {sub}")
            row, col = sub
            if row < len(map) and col < len(map) and col >= 0 and row >= 0:
                map[row][col] = "#"
        
for row in map:
    print(row)

sub_count = 0
for row in map:
    for char in list(row):
        if char == "#":
            sub_count+=1
        
print(f"Substations: {sub_count}")
