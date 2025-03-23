from typing import List, Optional

from interviewmaster.TreeNode import TreeNode


class Solution:
    
    def preorderDFS(self, root: Optional['TreeNode']) -> List[TreeNode]:
        result = []

        def dfs(root):
            if not root:
                return None
        
            result.append(root)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return result



    def flatten(self, root: Optional['TreeNode']) -> None:
        if not root:
            return
        
        nodes = self.preorderDFS(root)
        current = root
        for node in nodes:
            current.left = None
            current.right = node
            current = node
        current.left = None
        current.right = None
        
       
       
       