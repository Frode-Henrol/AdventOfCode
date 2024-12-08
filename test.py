from itertools import combinations

# Example coordinates
coordinates = [(1, 2), (3, 4), (5, 6)]

# Find all pair combinations (order is irrelevant)
pairs = list(combinations(coordinates, 2))

print(pairs)