package com.nav;

public class CycleLinkedList {

    class ListNode {

        int val;
        ListNode next;

        public ListNode(int val) {
            this.val = val;
            this.next = null;
        }
    }

    public boolean hasCycle(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;

        while (true) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                return true;
            }

            if (slow == null || fast == null) return false;

        }


    }


}
