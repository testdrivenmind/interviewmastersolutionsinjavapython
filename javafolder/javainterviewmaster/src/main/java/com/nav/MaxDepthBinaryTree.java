package com.nav;

import java.util.LinkedList;
import java.util.Queue;

public class MaxDepthBinaryTree {

    class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        public TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public int maxDept(TreeNode root) {
        if (root == null) {
            return 0;
        }

        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        int depth = 0;
        while (!q.isEmpty()) {
            int size = q.size();
            depth++;
            for (int i = 0; i < size; i++) {
                TreeNode removedNode = q.poll();
                if (removedNode.left != null) q.offer(removedNode.left);
                if (removedNode.right != null) q.offer(removedNode.right);
            }

        }

        return depth;
    }

    public int maxDepthDFS(TreeNode root) {

        if (root == null) {
            return 0;
        }

        return 1 + Math.max(maxDepthDFS(root.left), maxDepthDFS(root.right));
    }

}
