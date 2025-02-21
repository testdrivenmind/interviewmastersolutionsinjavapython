package com.nav;

public class DiameterOfBinaryTree {
    int maxDiameter = 0;


 class TreeNode {

    int val;
    TreeNode left;
    TreeNode right;

    public TreeNode(int val) {
        this.val = val;
    }

    public TreeNode (int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}


    
    public int diameterOfBinaryTree(TreeNode root) {
        
        computeHeight(root);
        return maxDiameter;
                
            }
        
        
        
    private int computeHeight(TreeNode node) {

        if (node == null) {
            return 0;
        }

        int leftHeight = computeHeight(node.left);
        int rightHeight = computeHeight(node.right);

        maxDiameter = Math.max(maxDiameter, leftHeight + rightHeight);

        return 1 + Math.max(leftHeight, rightHeight);
    }
}
