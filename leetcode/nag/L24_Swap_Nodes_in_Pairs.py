# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        answer = head.next
        prev = ListNode(0, head)
        while head and head.next:
            prev.next = head.next
            head.next.next, head.next = head, head.next.next
            head = head.next
            prev = prev.next.next
        return answer
