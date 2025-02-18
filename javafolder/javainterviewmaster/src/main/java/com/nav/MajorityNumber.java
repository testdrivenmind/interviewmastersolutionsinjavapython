package com.nav;

public class MajorityNumber {

    public int majorityNumber(int[] nums) {

        int candidate = nums[0];
        int count = 1;
        for (int num : nums) {
            if (num == candidate) {
                count++;
            } else {
                count--;
                if (count == 0) {
                    candidate = num;
                    count = 1;
                }
            }
        }
        return candidate;
    }

    public int majorityNumber1(int[] nums) {

        int candidate = nums[0];
        int count = 1;
        for (int num : nums) {
            if (count == 0) {
                candidate = num;
            }
            count += (num == candidate) ? 1 : -1;
        }
        return candidate;
    }
}
