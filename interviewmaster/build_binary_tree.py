from typing import List, Optional

from interviewmaster.TreeNode import TreeNode



class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional['TreeNode']:

        if not preorder or not inorder:
            return None
        
        root_val = preorder[0]
        root = TreeNode(root_val)
        root_index_in_inorder = inorder.index(root_val)

        root.left = self.buildTree(preorder[1: 1 + root_index_in_inorder], inorder[:root_index_in_inorder])
        root.right = self.buildTree(preorder[1 + root_index_in_inorder:], inorder[1 + root_index_in_inorder:])
    
        return root
    

    def buildTreeFromPostOrder(self, postorder: List[int], inorder: List[int]) -> Optional['TreeNode']:
        if not postorder or not inorder:
            return None
    
        root_val = postorder.pop()
        root = TreeNode(root_val)
        root_index_in_order = inorder.index(root_val)

        root.right = self.buildTree(inorder[root_index_in_order + 1:], postorder)
        root.left = self.buildTree(inorder[:root_index_in_order], postorder)
        return root


nums = [10,20,30,40,50]
forward_index = [0,1,2,3,4]
backward_index = [-5,-4,-3,-2,-1]

print("********")
print(nums[len(nums) - 1:len(nums) - 2:-1])
