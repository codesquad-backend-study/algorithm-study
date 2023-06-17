# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        queue = []
        intermediate = []
        for node in lists:
            temp = []
            while node is not None:
                temp.append(node)
                node = node.next
            intermediate.append(temp)
        for temp in intermediate:
            queue = list(heapq.merge(queue, temp, key=lambda x : x.val))
        for index in range(len(queue) - 1):
            queue[index].next = queue[index + 1]
        if not queue:
            return None
        queue[len(queue) - 1].next = None
        return queue[0]
