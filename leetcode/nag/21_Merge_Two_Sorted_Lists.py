# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list = []
        
        if not list1 and not list2:
            return None
        pointer = list1

        while pointer:
            list.append(pointer)
            pointer = pointer.next
        pointer = list2
        while pointer:
            list.append(pointer)
            pointer = pointer.next
        list.sort(key = lambda element: element.val)
        for index in range(len(list) - 1):
            list[index].next = list[index + 1]
        return list[0]
      
