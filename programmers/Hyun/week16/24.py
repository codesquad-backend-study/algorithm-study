# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        prev = ListNode()
        prev.next = head
        cur = head

        ans = head
        next_node = None
        if head.next != None:
            ans = head.next
            next_node = head.next

        while prev.next != None and prev.next.next != None:
            cur = prev.next
            next_node = prev.next.next

            cur.next = next_node.next
            next_node.next = cur
            prev.next = next_node

            prev = cur

        return ans
