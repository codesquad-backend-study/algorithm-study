# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        node = None
        if not list1:
            return list2

        if not list2:
            return list1

        if list1.val >= list2.val:
            head = node = list2
            list2 = list2.next
        else:
            head = node = list1
            list1 = list1.next

        while list1 and list2:
            if list1.val >= list2.val:
                node.next = list2
                node = node.next
                list2 = list2.next
            else:
                node.next = list1
                node = node.next
                list1 = list1.next

        if list1:
            node.next = list1

        if list2:
            node.next = list2

        return head
