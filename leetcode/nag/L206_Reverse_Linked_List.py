# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        pointer = head
        list = []
        if len(list) == 1:
            return head
        while pointer:
            list.append(pointer)
            pointer = pointer.next
        for index in range(len(list) - 1, -1, -1):
            if index == 0:
                list[index].next = None
                break
            list[index].next = list[index - 1]
        return list[-1]
