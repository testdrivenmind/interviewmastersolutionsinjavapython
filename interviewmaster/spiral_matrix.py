from typing import List


class Solution:

    def spiralMatrix(self, matrix: List[List[int]]) -> List[int]:
        """
        docstring
        """
        # matrix is null
        if not matrix:
            return []
        
        # row length is 1
        if len(matrix) == 1:
            return matrix[0]
        
        # column length is 1
        if len(matrix[0]) == 1:
            return [row[0] for row in matrix]
    
        # taking the first row
        first_row = matrix[0]

        # taking the last column exclusing the one in the first row since it would be already taken by the first row
        last_column = [row[-1] for row in matrix[1::]] 

        # taking the last row in reverse from right to left, if more than one row remains
        last_row = matrix[-1][:-1:][::-1] if len(matrix) > 1 else []

        # taking the last column in reverse if more than 2 rows exsist
        first_column = [ row[0] for row in matrix[-2:0:-1]] if len(matrix) > 2 else []

        # extracting the inner matrix by removing first row, last column, last row and first column
        inner_matrix = [[row[1:-1] for row in matrix[1:-1]] if len(row[1:-1]) > 0]

        return first_row + last_column + last_row + first_column + self.spiralMatrix(inner_matrix)


sm = Solution()
data1 = [
        [1,2,3]
]

data2 = [
    [1]
]

data3 = [
    [1,2],
    [2,2]
]
print(data2[0])
print(f"lenth: {len(data2[0])}")
print(data3[0])
print(f"lenth: {len(data3[1])}")

# print(sm.spiralMatrix(data2))
