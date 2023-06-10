import heapq
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # k개 오름차순 -> 정렬된 하나의 연결된 목록으로 병합하여 반환
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        head = tail = ListNode(0, None)

        for i, li in enumerate(lists):
            if li:
                heapq.heappush(h, (li.val, i, li))

        while h:
            popped = heapq.heappop(h)
            INDEX = 1
            LIST = 2
            index = popped[INDEX]
            node = popped[LIST]
            tail.next = node
            tail = tail.next

            if node.next:
                heapq.heappush(h, (node.next.val, index, node.next))

        return head.next
