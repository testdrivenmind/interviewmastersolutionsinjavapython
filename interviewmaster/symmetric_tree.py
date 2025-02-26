
from collections import deque
from typing import Optional

from interviewmaster.TreeNode import TreeNode


class Solution:

    def is_symmetric(self, root: Optional["TreeNode"]) -> bool:
        # initialize the queue with left and right
        if not root:
            return True
        
        if root.left and root.right:
            q = deque([(root.left, root.right)])
        
        while q:
                leftNode, rightNode = q.popleft()

                if not leftNode and not rightNode:
                    continue
                
                if not leftNode or not rightNode or leftNode.val != rightNode.val:
                    return False
                q.append((leftNode.left, rightNode.right))
                q.append((leftNode.right, rightNode.left))
        return True
    
    def r_is_symmetric(self, root: Optional["TreeNode"]) -> bool:
        if not root:
              return True
        def is_mirror(left, right):
              
            if not left and not right:
                return True

            if not left or not right:
                return False

            return (left.val == right.val and 
                is_mirror(left.left, right.right) and 
                is_mirror(left.right, right.left))
        
        return is_mirror(root.left, root.right)