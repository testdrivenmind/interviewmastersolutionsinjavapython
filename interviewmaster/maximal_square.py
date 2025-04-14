# question
#  we need to find the largest square in the region with only ones and return area which is side * side or length * breadth, where length and breadh are equal
# approach
#  if empty matrix, area becomes 0, if [[1]] area is 1
# solution
# complexity


from typing import List

class Solution:

    def maximum_square(self, matrix: List[List[str]]) -> int:

        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[0] * (cols+1) for _ in range(rows+1)]
        max_side = 0

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "1":
                    dp[r+1][c+1] = min(dp[r][c], dp[r+1][c], dp[r][c+1]) + 1
                    max_side = max(max_side, dp[r+1][c+1])
        return max_side * max_side
    

    # def maximum_square_bf(self, matrix: List[list[int]]) -> int:

sol = Solution()
m = [['1', '1'],['1', '1']]
print(sol.maximum_square(m))