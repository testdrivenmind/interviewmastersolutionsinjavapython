
// -3 - get min - still in the stack - removed by pop but doesnt return
// -2 
// 0 - this is the top element on the stack - gets it


// [-2, 0]
// 0 
// -2
// - 3 - get min - still in the stack - 

package com.nav;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class MinStack {

    int val;
    List<Integer> mainStack = new ArrayList<>();
    Stack<Integer> minStack = new Stack<>();

     public MinStack() {};

     public void push(int val) {
        this.val = val;
        mainStack.add(val);
        int minVal = Math.min(val, minStack.isEmpty() ? val : minStack.peek());
        minStack.push(minVal);
    };


    public void pop() {
        int remove = mainStack.size() - 1;
        mainStack.remove(remove);
        mainStack.remove(remove);
    }

    public int top() {
        return mainStack.get(mainStack.size() - 1);

    }

    public int getMin() {
        return minStack.peek();
    }

}