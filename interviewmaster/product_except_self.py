from typing import List


class Solution:

    def product_except_self(self, nums: list[int]) -> list[int]: 
        # [1,2,3,4]
        n = len(nums)
        answer = [1] * n
        left_product = 1

        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]
            
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]
        return answer




    def product_except_self1(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        right = [1] * n
        result = [1] * n
    
        for i in range(1,n):
            left[i] = left[i - 1] * nums[i -1]
        
        for i in range(n-2, -1, -1):
             right[i] = right[i+1] * nums[i+1]

        for i in range(n):
             result[i] = left[i] * right[i]
        return result 




if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,4]
    print(sol.product_except_self1(nums))