package com.nav;

import java.util.ArrayList;
import java.util.List;

public class MaximumSubArraySum {
    
    public static int MaximumSubArraySum(int[] nums) {

    
        int current_sum = nums[0];
        int max_sum = current_sum;

        for (int i = 1; i < nums.length; i++) {
            if (current_sum + nums[i] < nums[i] ) {
                current_sum = nums[i];
            } else {
                current_sum += nums[i];
            }
            
            max_sum = Math.max(max_sum, current_sum);
        }
        
        return max_sum;
        
    }

    public static void main(String[] args) {
        System.out.println(MaximumSubArraySum(new int[]{1}));
    }
}
