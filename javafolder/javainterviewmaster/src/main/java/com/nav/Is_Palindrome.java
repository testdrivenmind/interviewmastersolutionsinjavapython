package com.nav;

public class Is_Palindrome {

    public boolean isPalindrome(String s) {
        s = s.toLowerCase();
        System.out.println(s);
        int left = 0;
        int right = s.length() - 1;
        while (left < right) {
            char left_char = s.charAt(left);
            char right_char = s.charAt(right);

            if (!Character.isLetterOrDigit(left_char)) {
                left++;
            } else if (!Character.isLetterOrDigit(right_char)) {
                right--;
            } else if (s.charAt(left) != s.charAt(right)) {
                return false;
            } else {
                left++;
                right--;
            }

        }
        return true;
    }
}
