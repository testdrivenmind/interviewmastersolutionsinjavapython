


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


def merge_two_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

    # iterate through the first and second list
    # compare the values on each node, if something is lesser, push it to the current and move
    # once one of the listnodes is emptied, put all the remaining into the current



    current = ListNode()
    dummy = current

    while list1 and list2 :

        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

    current = current.next    

    if list1:
        current.next = list1
          
    
    if list2:
        current.next = list2

    return dummy.next