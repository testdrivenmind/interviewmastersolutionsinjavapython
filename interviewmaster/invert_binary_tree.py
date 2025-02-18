
from collections import deque
from typing import Optional


class TreeNode:
    val: int
   

    def __init__(self, val: int, left: Optional["TreeNode"]=None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right



    def swapNode(self):
        self.left, self.right = self.right, self.left

def  invert_binary_tree(root: TreeNode):

    q = deque([root])
    
    while q:
        removedNode = q.popleft()
        removedNode.swapNode()
        if removedNode.left:
            q.append(removedNode.left)
        if removedNode.right:
            q.append(removedNode.right)
    return root

    
