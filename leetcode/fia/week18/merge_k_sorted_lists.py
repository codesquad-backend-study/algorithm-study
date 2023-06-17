# Definition for singly-linked list.
from typing import List, Optional
from heapq import heappush, heappop, heapify


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        all_nodes = []
        for head in lists:
            temp = head
            while temp:
                all_nodes.append(head)
                temp = temp.next

        if not all_nodes:
            return None

        heap = []
        for index, node in enumerate(all_nodes):
            heappush(heap, (node.val, index, node))

        head = heappop(heap)[2]
        current_node = head
        while heap:
            if current_node:
                popped_node = heappop(heap)[2]
                current_node.next = popped_node
                current_node = popped_node

        return head




