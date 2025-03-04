from typing import List


class Solutiion:

    def contains_duplicates(self, nums: List[int]) -> bool:
        """
        docstring
        """
        unique_nums = set(nums)
        return len(nums) == len(unique_nums)
        
    @staticmethod
    def contains_duplicates1(self, nums: List[int]) -> bool:
        """
        docstring
        """
        unique_nums = set()

        for num in nums:
            if num in unique_nums:
                return True
            else:
                unique_nums.add(num)
        return False