# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        if head.next == None:
            return head

        odd = head
        even_head = even = odd.next

        while True:
            odd.next = even.next
            if even.next == None:
                break
            odd = odd.next

            even.next = odd.next
            if odd.next == None:
                break
            even = even.next

        odd.next = even_head
        return head
