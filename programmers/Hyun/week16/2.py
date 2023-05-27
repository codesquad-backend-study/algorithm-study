# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = collections.deque()
        while l1 != None:
            num1.appendleft(l1.val)
            l1 = l1.next
        num1 = int(''.join(map(str, num1)))

        num2 = collections.deque()
        while l2 != None:
            num2.appendleft(l2.val)
            l2 = l2.next
        num2 = int(''.join(map(str, num2)))

        summ = list(str(num1 + num2))
        summ = list(map(int, summ))

        head = cur = ListNode(summ.pop(), None)
        while summ:
            cur.next = ListNode(summ.pop(), None)
            cur = cur.next

        return head
