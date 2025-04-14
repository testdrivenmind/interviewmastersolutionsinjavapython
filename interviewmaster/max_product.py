# intuition
    # have two pointers left and right
    # have max_product as 1
    # max_length as 0
    # traverse via the list and calculate the max product, max length and check which is bigger
    # if product is less than max, then reset the produc to 0, also, move the left pointer to the right and move on
    #  return the max product
# approach

# time complexity

from typing import List


class Solution:
    
    def max_product(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        curr_max = nums[0]
        curr_min = nums[0]
        global_max = nums[0]
        
        for i in range(1, len(nums)): 
            n = nums[i]

            if n < 0:
                curr_max, curr_min = curr_min, curr_max

            curr_max = max(n, curr_max * n)
            curr_min= min(n, curr_min * n)

            global_max = max(global_max, curr_max)
        
        return global_max
    
sol = Solution()

print(sol.max_product([2,3,-2,4]))
print(sol.max_product([-2,0,-1]))
# failing for this case, how to fix it
print(sol.max_product([0,2])) 