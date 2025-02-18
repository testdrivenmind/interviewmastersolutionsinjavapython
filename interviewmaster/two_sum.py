
from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    
    sum_map = {}
    for index, num in enumerate(nums):
        missing_num = target - num
        if missing_num in sum_map:
            return [index, sum_map[missing_num] ]
        else:
            sum_map[num] = index

