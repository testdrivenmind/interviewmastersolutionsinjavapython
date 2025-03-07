from collections import deque
import heapq
from typing import Optional


class Solution:

    def kth_smallest(self, root: Optional[TreeNode], k: int) -> int:
       
        min_heap = []
        
        def dfs(node):
            if node is None:
                return
         
            heapq.heappush(min_heap, node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
       
        return heapq.nsmallest(k, min_heap)[-1]
       
