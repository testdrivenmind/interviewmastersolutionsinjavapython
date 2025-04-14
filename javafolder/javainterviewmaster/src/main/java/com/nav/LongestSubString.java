package com.nav;

import java.util.HashMap;
import java.util.HashSet;
import java.util.stream.Collectors;

public class LongestSubString {
    

    private int longestSubString(String s) {
       
        if (s.length() == 1 || s.length() == 0) return s.length();

        HashSet<Character> s_new = s.chars()
                                        .mapToObj(c -> (char) c)
                                        .collect(Collectors.toCollection(HashSet::new));

        if (s_new.size() == s.length()) return s.length();
        
        HashSet<Character> charSet = new HashSet<>();
        int left = 0;
        int max_length = 0;

        for (int right = 0; right < s.length(); right++) {
             while (charSet.contains(s.charAt(right))) {
                    charSet.remove(s.charAt(left));
                    left++;
             }
            charSet.add(s.charAt(right));

            max_length = Math.max(max_length, right - left + 1);
        }

        return max_length;


    }


    private int longestSubString_sol2(String s) {

        HashMap<Character, Integer> charMap = new HashMap<>();

        int start = 0; // start of current substring
        int max_length = 0;

        for (int i = 0; i < s.length(); i++) {
            Character element = s.charAt(i);
            if (charMap.containsKey(element) && charMap.get(element) >= start) {
                start = charMap.get(element) + 1;
            } else {
                max_length = Math.max(max_length, charMap.get(element)- start + 1);
            }

            charMap.put(element, i);
            
        }

        return max_length;

    }

    public static void main(String[] args) {
        
        LongestSubString sol = new LongestSubString();
        System.out.println(sol.longestSubString("abcabcbb"));
       
        
    }

}


