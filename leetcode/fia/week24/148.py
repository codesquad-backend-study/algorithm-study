# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        nodes = []
        node = head
        while node:
            nodes.append(node)
            node = node.next

        nodes.sort(key=lambda x: (x.val))

        nodes[-1].next = None
        head = nodes[0]
        node = head
        for n in nodes[1:]:
            node.next = n
            node = n

        return head
