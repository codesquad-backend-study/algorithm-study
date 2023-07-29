# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        linked_to = []
        cur = head
        while cur:
            linked_to.append(cur.val)
            cur = cur.next

        for i in range(1, len(linked_to)):
            # i부터 1까지 -1(감소)씩 반복
            for j in range(i, 0, -1):
                # 한 칸씩 왼쪽으로 이동
                if linked_to[j] < linked_to[j - 1]:
                    linked_to[j], linked_to[j - 1] = linked_to[j - 1], linked_to[j],
                    continue

                break

        new_head = ListNode(linked_to[0])
        cur = new_head
        # 첫번째(0)는 new_head로 이미 소비되었으므로 두번째(1)부터
        for val in linked_to[1:]:
            # 새로운 노드를 생성 후 다음 노드를 가리키도록 함
            cur.next = ListNode(val)
            cur = cur.next

        return new_head
