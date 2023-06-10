# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        idx = 0
        for each in lists:
            if not each:
                continue

            cur = each
            while cur:
                heappush(heap, (cur.val, idx, cur))
                cur = cur.next
                idx += 1

        if not heap:
            return None

        head = heappop(heap)[2]
        cur = head
        while heap:
            cur.next = heappop(heap)[2]
            cur = cur.next
        cur.next = None

        return head
