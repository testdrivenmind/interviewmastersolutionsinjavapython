package com.nav;


import java.util.LinkedList;
import java.util.Queue;

public class InvertBinaryTree {

    class TreeNode {

        int val;
        TreeNode left;
        TreeNode right;

        public TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;

        }

        public TreeNode(int val) {
            this.val = val;
        }
    }


    public TreeNode invertTree(TreeNode root) {
        if (root == null) {
            return root;
        }

        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            TreeNode removedNode = q.poll();
            swapNodes(removedNode);

            if (removedNode.left != null) {
                q.add(removedNode.left);
            }
            if (removedNode.right != null) {
                q.add(removedNode.right);
            }

        }
        return root;
    }


    private void swapNodes(TreeNode current) {
        TreeNode temp = current.left;
        current.left = current.right;
        current.right = temp;

    }
}
