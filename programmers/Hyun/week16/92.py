# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional:
        cnt = 1
        left_prev = right_next = None
        left_node = right_node = None

        cur = head
        while cur != None and cnt <= right + 1:
            if cnt == left - 1:
                left_prev = cur

            if cnt == left:
                left_node = cur

            if cnt == right:
                right_node = cur

            if cnt == right + 1:
                right_next = cur

            cur = cur.next
            cnt += 1

        prev = right_next
        cur = left_node
        for _ in range(right - left + 1):
            next_node = cur.next
            cur.next = prev

            prev = cur
            cur = next_node

        if left_prev != None:
            left_prev.next = right_node
        else:
            head = right_node

        return head
