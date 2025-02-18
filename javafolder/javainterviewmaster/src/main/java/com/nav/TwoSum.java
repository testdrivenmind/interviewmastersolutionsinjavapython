package com.nav;

import java.util.*;

public class TwoSum {

    private int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map_sum = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complementary_num = target - nums[i];
            if (map_sum.containsKey(complementary_num)) {
                return new int[] {i, map_sum.get(complementary_num)};
            }
            map_sum.put(nums[i], i);
        }

        return null;
    }


    
}
