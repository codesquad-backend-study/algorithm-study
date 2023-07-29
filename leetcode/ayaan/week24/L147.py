# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head.next
        sort_head = sort_cur = ListNode(cur.val)
        prev = None
        while cur:
            while sort_cur:
                if cur.val < sort_cur.val:
                    if prev:
                        prev.next = ListNode(cur.val)
                        prev.next.next = sort_cur
                        break
                    else:
                        prev = ListNode(cur.val)
                        prev.next = sort_cur
                        break
                sort_cur = sort_cur.next
            cur = cur.next
            sort_cur = sort_head
        return sort_head
