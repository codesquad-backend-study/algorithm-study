# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        linked_to = head
        while linked_to:
            arr.append(linked_to.val)
            linked_to = linked_to.next

        arr.sort()

        linked_from = head
        for x in arr:
            linked_from.val = x
            linked_from = linked_from.next

        return head
