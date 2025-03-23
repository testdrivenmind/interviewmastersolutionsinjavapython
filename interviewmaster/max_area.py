from typing import List


class Solution:
    
    def max_area(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left <= right:
            min_height = min(height[left], height[right])
            distance = right - left
            max_area = max(max_area, min_height * distance)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
    
sol = Solution()
heights = [1,8,6,2,5,4,8,3,7]
print(sol.max_area(heights))