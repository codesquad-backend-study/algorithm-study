from typing import Optional

from leetcode.fia.week16.merge_two_sorted_lists import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        tail = None
        next_node = None
        node = head

        while node is not None:
            next_node = node.next
            node.next = tail
            tail = node
            node = next_node

        return tail
