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


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur:
            next_node = cur.next

            cur.next = prev

            prev = cur
            cur = next_node

        return prev
