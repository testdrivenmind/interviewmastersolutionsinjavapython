from typing import List


class Solution:
    def three_sum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1    
                    left += 1
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    right -= 1
        return result
    
sol = Solution()
eg1 = [-1,0,1,2,-1,-4]
eg2 = [0,1,1]
eg3 = [0,0,0]
eg4 = [2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]
print(sol.three_sum(eg1)) 
print(sol.three_sum(eg2)) 
print(sol.three_sum(eg3)) 
print(sol.three_sum(eg4)) 
