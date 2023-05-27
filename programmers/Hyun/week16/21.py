# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []

        while list1 != None:
            nodes.append((list1.val, list1))
            list1 = list1.next

        while list2 != None:
            nodes.append((list2.val, list2))
            list2 = list2.next

        nodes.sort(key=lambda x: x[0])

        if not nodes:
            return None

        head = nodes[0][1]
        tmp = nodes[0][1]
        for _, node in nodes[1:]:
            tmp.next = node
            tmp = tmp.next

        return head
