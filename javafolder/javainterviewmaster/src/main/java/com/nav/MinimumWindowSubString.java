package com.nav;

import java.util.HashMap;

public class MinimumWindowSubString {

    private String minimumWindowSubstring(String s, String t) {

        if(s == null || t == null || s.length() < t.length() ) return "";

        HashMap<Character, Integer> t_map = new HashMap<>();
        for (Character element : t.toCharArray()) {
                t_map.put(element, t_map.getOrDefault(element, 0) + 1);
        }
        HashMap<Character, Integer> window = new HashMap<>();

        int left = 0;
        int start = -1;
        int end = -1;
        int res_len = Integer.MAX_VALUE;
        int have = 0;
        int need = t_map.size();

        for (int right = 0; right < s.length(); right++) {
                char charS = s.charAt(right);
                window.put(charS, window.getOrDefault(charS, 0) + 1);

                if (t_map.containsKey(charS) && t_map.get(charS) == window.get(charS)) have ++;

                while (have == need) {
                    if (right - left + 1 < res_len) {
                        start = left;
                        end = right;
                        res_len = right - left + 1;
                        
                    }
                    char charSleft = s.charAt(left);
                    window.put(charSleft, window.get(charSleft) - 1); 

                    if (t_map.containsKey(charSleft) && window.get(charSleft) < t_map.get(charSleft) ) have--;
                    left++;
                    
                }
                
            }
            return res_len == Integer.MAX_VALUE ? "" : s.substring(start, end + 1);

    }

    public static void main(String[] args) {
        
        MinimumWindowSubString sol = new MinimumWindowSubString();
        System.out.println(sol.minimumWindowSubstring("ADOBECODEBANC", "ABC"));
    }
}