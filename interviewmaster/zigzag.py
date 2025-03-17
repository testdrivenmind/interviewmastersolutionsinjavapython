from collections import deque
from typing import List, Optional

from interviewmaster.TreeNode import TreeNode


class Solution:
    def zigzagLevelOrderTraversal(self, root: Optional["TreeNode"]) -> List[List[int]]:
        if root:
            q = deque([root]) # type: ignore
        else:
            return []
        result = []
        left_to_right = True

        while q:
            level_size = len(q)
            current_level_list = []
                
            for _ in range(level_size):
                node = q.popleft()
                current_level_list.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

            if not left_to_right:
                current_level_list.reverse()

            result.append(current_level_list)
            left_to_right = not left_to_right

        return result

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(sol.zigzagLevelOrderTraversal(root))