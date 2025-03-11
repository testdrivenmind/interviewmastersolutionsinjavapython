matrix = [[10,20, 30], [11,12,31]]


for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        print(f"{[row]} {[col]} = {matrix[row][col]}")

print("see the difference between for number of visits")

for row_index, row_list in enumerate(matrix):
    for col_index, val in enumerate(row_list):
        print(f"{[row_index]} {[col_index]} = {val}")