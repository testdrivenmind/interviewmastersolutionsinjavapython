from collections import deque
import heapq
from typing import List


class Solution:

    def kth_largest_element(self, nums: List[int], k: int) -> int:
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, -num)
        print(min_heap)
        for i in range(k):
            heapq.heappop(min_heap)
        return -min_heap[0]    
sol = Solution()
print(sol.kth_largest_element([3,2,1,5,6,4], 2))