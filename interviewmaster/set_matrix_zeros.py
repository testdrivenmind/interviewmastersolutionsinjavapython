from typing import List


# class Solution:

#     def set_zeros(self, matrix: List[List[int]]) -> None:



matrix = [
        [10,20,30,40],
        [19,20,21,24],
        [89,78,67,48]
]

for row in matrix:
    print(row)

for row_index, row_list in enumerate(matrix):
    print(f"{row_index} -> {row_list}")

for row_index, row_list in enumerate(matrix):
    for col_index, col in enumerate(row_list):
        print(f"{[row_index]}{[col_index]} -> {col}")

for col_index in range(len(matrix[0])):
    col_list = [row[col_index] for row in matrix]
    print(f"{col_index} -> {col_list}")

nums1 = [20,30,40]
nums2 = [21,31,40]
print(*zip(nums1,nums2))

print(zip(matrix))
print(*zip(matrix))
print(list(zip(*matrix)))