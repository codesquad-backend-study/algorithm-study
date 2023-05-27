# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        nodes = []
        while head != None:
            nodes.append(head)
            head = head.next

        if not nodes:
            return None

        head = cur = nodes[-1]
        for node in nodes[::-1][1:]:
            cur.next = node
            cur = cur.next

        cur.next = None
        return head
