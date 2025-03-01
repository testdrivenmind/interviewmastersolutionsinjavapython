from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        previous_max = 0
        current_max = 0
        while num in nums:
            new_max = max(current_max, previous_max + num)
            previous_max = current_max
            current_max = new_max
        return current_max
              
    
        
           


if __name__ == "__main__":
    sol = Solution()
    print(sol.rob([2,1,1,2]))