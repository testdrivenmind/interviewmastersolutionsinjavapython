from typing import List


class Solution:
    def max_profit(self, prices: List[int]) -> int:
        """
        docstring
        """
        max_profit: int = 0
        total_profit: int = 0
        min_pice: int = prices[0]

        for price in prices:
            min_pice = min(min_pice, price)
            profit: int = price - min_pice
            if profit > 0:
               total_profit += profit
               min_pice = price
        return total_profit
    

if __name__ == "__main__":
    sol = Solution()
    # nums = [7,1,5,3,6,4]
    nums = [1,2,3,4,5]
    print(sol.max_profit(nums))