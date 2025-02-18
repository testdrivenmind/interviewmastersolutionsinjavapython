

from collections import deque
from typing import Optional


class TreeNode:
   
    def __init__(self, val: int, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def max_depth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.max_depth(root.left), self.max_depth(root.right))


    def max_depth_bfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q: deque = deque([root])
        depth: int = 0
        while q:
            depth += 1
            for _ in list(q):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return depth