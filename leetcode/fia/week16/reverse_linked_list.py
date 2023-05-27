from typing import Optional

from leetcode.fia.week16.merge_two_sorted_lists import ListNode


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    tail = None
    node = head

    while node is not None and node.next is not None:
        temp = node.next
        node.next = tail
        tail = node
        node = temp

    return node
