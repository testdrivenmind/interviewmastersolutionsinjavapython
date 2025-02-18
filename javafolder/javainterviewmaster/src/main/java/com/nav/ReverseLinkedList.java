package com.nav;

class ListNode {

    int val;
    ListNode next;

    protected ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }

    protected ListNode(int val) {
        this.val = val;
    }

    protected ListNode() {
    }


}

public  class ReverseLinkedList {

    public static ListNode reverseLinkedList(ListNode head) {

        if (head == null || head.next == null) return head;
        ListNode temp = head;
        ListNode previous = null;
        ListNode after = head.next;

        while (head != null) {
            after = head.next;
            head.next = previous;
            previous = head;
            head = after;

        }

        return previous;
    }


    public static void main(String[] args) {

        ListNode node1 = new ListNode(10);
        ListNode node2 = new ListNode(20);
        ListNode node3 = new ListNode(30);
        node1.next = node2;
        node2.next = node3;
        printList(node1);
        node1 = reverseLinkedList(node1);
        System.out.println();
        System.out.println("******");
        printList(node1);

    }
        static void printList(ListNode head){
            while (head != null) {
                System.out.print(head.val + "-->");
                head = head.next;
            }
            System.out.print("null");
        }
    }

