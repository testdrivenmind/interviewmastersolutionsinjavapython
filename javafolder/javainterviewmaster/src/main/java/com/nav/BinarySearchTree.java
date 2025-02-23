package com.nav;

import java.util.ArrayDeque;
import java.util.Queue;

public class BinarySearchTree {
    

    public void inorderDepthFirstSearch(TreeNode root) {

        if (root == null) {
            return;
        }
        inorderDepthFirstSearch(root.left);
        System.out.println(root.val);
        inorderDepthFirstSearch(root.right);
    }

    public void preorderDepthFirstSearch(TreeNode root) {

        if (root == null) {
            return;
        }
        System.out.println(root.val);
        preorderDepthFirstSearch(root.left);
        preorderDepthFirstSearch(root.right);
    }

    public void postorderDepthFirstSearch(TreeNode root) {
        if (root == null) {
            return;
        }
        postorderDepthFirstSearch(root.left);
        postorderDepthFirstSearch(root.right);
        System.out.println(root.val);
    }


    public void breadthFirstSearch(TreeNode root) {

        Queue<TreeNode> q = new ArrayDeque<>();
        if (root != null) {
            q.add(root);
        }
        int level = 0;

        while (!q.isEmpty()) {
            System.out.println("level is:" + level);
            int levelLength = q.size();
            for (int i = 0; i < levelLength; i++) {
                TreeNode removedNode = q.poll();
                System.out.println(removedNode.val);
                if (removedNode.left != null) {
                    q.add(removedNode.left);
                }
                
                if (removedNode.right != null) {
                    q.add(removedNode.right);
                }
            }
            level++;
        }

    }


    public TreeNode insert(TreeNode root, int val) {

        if (root == null) {
            return new TreeNode(val);
        }

        if (val < root.val) {
            root.left = insert(root.left, val);
        } else if (val > root.val) {
            root.right = insert(root.right, val);
        } 
        return root;

    }

    public TreeNode remove(TreeNode root, int val) {

        if (root == null) {
            return null;
        }

        if (val > root.val){
            root.right = remove(root.right, val);
        } else if (val < root.val) {
            root.left = remove(root.left, val);
            
        } else{
            if (root.left == null) {
                return root.right;
            } else if (root.right == null) {
                return root.left;
            } else {
                int minValue = minValue(root.right);
                root.val = minValue;
                root.right = remove(root.right, minValue);
            }
        }

        return root;
    }


    private int minValue(TreeNode root) {
        if (root == null) {
            throw new IllegalArgumentException("current node cannot be null");
        }

        TreeNode current = root;
        while (current.left != null) {
            current = current.left;
        }
        return current.val;
    }


}
