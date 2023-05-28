# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []

        while head != None:
            values.append(head.val)
            head = head.next

        return values == values[::-1]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        prev = rev_head = None

        while fast and fast.next:
            rev_head = slow                 # 앞에서 rev_head = slow 를 하는 이유는, fast가 끝났을 때 rev_head는 slow 이전을 가리켜야 하기 때문

            fast = fast.next.next
            slow = slow.next                # slow 가 다음 노드 위치를 저장하는 temp 역할
            rev_head.next = prev            # 역순으로 연결 변경

            prev = rev_head

        if fast:
            slow = slow.next

        while rev_head and rev_head.val == slow.val:
            slow = slow.next
            rev_head = rev_head.next

        return not rev_head
