package com.nav;

import java.util.Arrays;

public class SortedArrayToBST {
    
    

    public TreeNode sortedArrayToBSD1(int[] nums) {
        
        if (nums == null || nums.length == 0) {
            return null;
        }

        int midPoint = nums.length / 2;
        int[] leftNums = Arrays.copyOfRange(nums, 0, midPoint);
        int[] rightNums = Arrays.copyOfRange(nums, midPoint + 1, nums.length);
        TreeNode root = new TreeNode(nums[midPoint]);
        root.left = sortedArrayToBSD1(leftNums);
        root.right = sortedArrayToBSD1(rightNums);
        return root;
    }


    public TreeNode sortedArrayToBSD(int[] nums) {
        int start = 0;
        int end = nums.length - 1;
        return rSortedArrayToBSD(nums, start, end);
                        
                    }
        
        
            private TreeNode rSortedArrayToBSD(int[] nums, int start, int end) {
                
                if (start > end) {
                    return null;
                }

                int midPoint = (start + end) / 2;
                TreeNode root = new TreeNode(nums[midPoint]);
                root.left = rSortedArrayToBSD(nums, start, midPoint - 1);
                root.right = rSortedArrayToBSD(nums, midPoint + 1, end);
                return root;
            
            
            }
        
        
        
// Tree Travesal, solve the problem not via recurrsion, write this solution in python, see the runtime in java
// have a look into the tree problems one more time


}
