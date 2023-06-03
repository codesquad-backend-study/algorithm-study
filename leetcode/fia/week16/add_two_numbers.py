from typing import Optional

from leetcode.fia.week16.merge_two_sorted_lists import ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l1
        rest = 0

        prev1 = None
        prev2 = None

        while l1 is not None and l2 is not None:
            val1 = val2 = None
            if l1 is None:
                val1 = 0
            else:
                val1 = l1.val
            if l2 is None:
                val2 = 0
            else:
                val2 = l2.val

            plus = val1 + val2  # 더하기 계산
            current = plus % 10  # 현재 노드의 값
            l1.val = current + rest  # 계산한 값 + 지난 올림 수
            rest = plus // 10  # 올림 수 다시 계산

            prev1 = l1
            prev2 = l2

            l1 = l1.next
            l2 = l2.next

        while l1 is not None:
            plus = l1.val + rest
            l1.val = plus % 10
            rest = plus // 10
            if l1.next is None and rest == 1:
                break
            l1 = l1.next

        if l2 is not None:
            prev1.next = l2

        if l1 is not None and rest == 1:
            l1.next = ListNode(1)

        if l2 is not None and rest == 1:
            l2.next = ListNode(1)

        return head

