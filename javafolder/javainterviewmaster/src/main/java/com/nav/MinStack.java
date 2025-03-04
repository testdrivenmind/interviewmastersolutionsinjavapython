
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

    //  have two array list, one for the order in which they came and one for storing the minimum value
    //  insertionOrderList just add the element and push
    //  for minOrderList, check the minValue before ordering and push the minValue to the last
    //  when poping if i need to pop the top value from insertionOrderList and wherever that specific value is there in the minOrderList
    // which cannot be o(1)
    // so another option to solve, this will be to have the index, of the minValue stored in dict and remove that index, will it be considered
    // o(1)
    // or should we go with some other data strucute like linkedlist
    // Input ["MinStack","push","push","push","getMin","pop","top","getMin"]
    // Input [[],[-2],[0],[-3],[],[],[],[]]
    // Output [null,null,null,null,-3,null,0,-2]


    // mainStack = [-2, 0 (as this is needs to be there for pop), -3]
    // minStack = [0,-2, -3 ]




    int val;
    List<Integer> mainStack = new ArrayList<>();
    Stack<Integer> minStack = new Stack<>();

     public MinStack() {};

     public void push(int val) {
        this.val = val;
        mainStack.add(val);
        if (minStack.isEmpty()) {
            minStack.add(val);
        } else {
            if (val < minStack.peek()) {
                minStack.push(val);
            } else {
                minStack.push(minStack.peek());
            }
        }
       
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