from typing import List, Optional
from interviewmaster.invert_binary_tree import TreeNode


class Solution:

    def r_sorted_array_to_bst1(self, nums, start, end):
        if start > end:
            return None
        mid_point: int = (start + end) // 2
        root: TreeNode = TreeNode(nums[mid_point])
        root.left = self.r_sorted_array_to_bst1(nums, start, mid_point - 1)
        root.right = self.r_sorted_array_to_bst1(nums, mid_point + 1, end)
        return root

    def sortedArrayToBST1(self, nums: List[int]) -> Optional[TreeNode]:
        start: int = 0
        end: int = len(nums) - 1
        return self.r_sorted_array_to_bst1(nums, start, end)
   
    def sorted_array_to_bst(self, nums: list[int]) -> Optional[TreeNode]:
        
        def helper(start: int, end: int):
            if start > end:
                return None
            mid_point: int = (start + end) // 2
            node: TreeNode = TreeNode(nums[mid_point])
            node.left = helper(start, mid_point - 1)
            node.right = helper(mid_point + 1, end)
            return node
        return helper(0, len(nums) - 1)