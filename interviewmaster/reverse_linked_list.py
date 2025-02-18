from typing import Optional


class ListNode:
    def __init__(self, val: int=0, next: Optional["ListNode"]=None) -> None:
        self.val = val
        self.next = next

def reverse_linked_list(head: ListNode) -> ListNode:
    previous: ListNode = None
    while head:
        after: ListNode = head.next
        head.next = previous
        previous = head
        head = after
    return previous
