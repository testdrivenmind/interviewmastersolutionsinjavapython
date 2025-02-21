package com.nav;

public class MiddleOfLinkedList {

    public ListNode middleOfLinkedList(ListNode head) {


        ListNode fast = head;
        ListNode slow = head;

        while(fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;

    }
    

}
