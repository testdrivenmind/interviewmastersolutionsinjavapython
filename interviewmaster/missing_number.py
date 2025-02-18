from typing import List


def missing_number1(nums: List[int]) -> int:
    max_num: int = max(nums)

    for num in range(0,max_num + 2):
        if num not in nums:
            return num
    return -1

def missing_number2(nums: List[int]) -> int:
    nums_set = set(nums)

    for num in range(len(nums) + 1):
        if num not in nums_set:
            return num
    return num

def missing_number(nums: List[int]) -> int:
    n: int = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


print(missing_number1([1]))
print(missing_number2([0]))