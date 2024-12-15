list2 = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0]]
list3 = [[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 1, 0]]

reversed_l = [li[::-1] for li in list2]
print(reversed_l)
print(list3)

if list3 == reversed_l:
    print("R")