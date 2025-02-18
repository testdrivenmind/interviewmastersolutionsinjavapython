from typing import List


def single_number(nums: List[int]) -> int:
   result: int = 0
   for num in nums:
      result ^= num
   return result 

    
