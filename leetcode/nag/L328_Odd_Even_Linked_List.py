# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answer = head
        if not head:
            return head
        init = head.next
        while head and head.next:
            nextHead = head.next
            head.next = head.next.next
            head = nextHead
        pointer = answer
        while pointer.next:
            pointer = pointer.next
        pointer.next = init
        return answer
      
