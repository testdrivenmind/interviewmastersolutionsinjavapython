package com.nav;

import java.util.HashMap;
import java.util.Map;

public class ValidAnagram {

    

    public boolean isValidAnagram(String s, String t) {

        if (s.length() != t.length()) return false;

        Map<Character, Integer> counter = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            char sChar = s.charAt(i);
            counter.put(sChar, counter.getOrDefault(sChar, 0) + 1);
        }

        for (int i = 0; i < s.length(); i++) {
            char tChar = t.charAt(i);
            if (counter.get(tChar) == null || counter.get(tChar) == 0) {
                return false;
            } else {
                counter.put(tChar, counter.get(tChar) - 1);
            }
        }

        return true;
    }
}
