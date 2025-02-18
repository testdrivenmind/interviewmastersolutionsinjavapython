package com.nav;

import java.util.*;

public class ValidParanthesis {

    public boolean isValid(String s) {

        Map<Character, Character> brackets = new HashMap<>();
        Deque<Character> bracesStack = new ArrayDeque<>();

        brackets.put('}', '{');
        brackets.put(']', '[');
        brackets.put(')', '(');

        for (int i = 0; i < s.length(); i++) {
            char current = s.charAt(i);

            if (brackets.containsKey(current)) {
                if (bracesStack.isEmpty() || bracesStack.peek() != brackets.get(current)) {
                    return false;
                }
                bracesStack.pop();
            } else {

            bracesStack.push(current);
        }
            }

        return bracesStack.isEmpty();

    }
}
