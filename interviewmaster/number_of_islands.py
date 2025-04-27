from typing import List


class Solution:
    # Intuition
# <!-- Describe your first thoughts on how to solve this problem. -->

# Approach
# <!-- Describe your approach to solving the problem. -->

# Complexity
# - Time complexity:
# <!-- Add your time complexity here, e.g. $$O(n)$$ -->

# - Space complexity:
# <!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
    
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        num_of_islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    num_of_islands += 1
                    queue = [(r,c)]
                    grid[r][c] = "0" #mark visited

                    while queue:
                        (row, col) = queue.pop(0)
                        # check all four neighbours
                        for (dr,dc) in [(-1,0),(1,0),(0,-1),(0,1)]:
                            nr = row + dr
                            nc = col + dc
                            if 0 <= nr < rows and 0 <= nr < cols and grid[nr][nc] == "1":
                                queue.append((nr,nc))
                                grid[nr][nc] = "0" #mark visited

        return num_of_islands