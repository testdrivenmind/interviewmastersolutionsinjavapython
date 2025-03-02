package com.nav;

public class VaidBinarySearchTree {
    
    public boolean isVaidBST(TreeNode root) {



        return helper(root, Long.MIN_VALUE, Long.MAX_VALUE);


}

    private boolean helper(TreeNode node, long lowerBound, long upperBound) {

            if (node == null) {
                return true;
            }


            if (node.val <= lowerBound || node.val >= upperBound) {
                    return false;
            }

            return (helper(node.left, lowerBound, node.val) && helper(node.right, node.val, upperBound));
            


            
    }


}
