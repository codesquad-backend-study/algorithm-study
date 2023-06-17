import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, item in enumerate(lists):
            j = 0
            while item != None:
                heapq.heappush(heap, (item.val, i, j, item))
                item = item.next
                j += 1

        if not heap:
            return None

        head = node = heapq.heappop(heap)[3]
        while heap:
            node.next = heapq.heappop(heap)[3]
            node = node.next
        return head
