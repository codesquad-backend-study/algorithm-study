class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # head = pointer = ListNode()
        # temp = 0
        # while l1 or l2:
        #     if not l1 or not l2: # 둘 중 하나 None
        #         num = l1.val + temp if l1 else l2.val + temp
        #     else: # 둘다 None이 아닐때
        #         num = l1.val + l2.val + temp
        #     temp = num // 10
        #     num = num % 10
        #     pointer = pointer.next
        #     pointer = num
        #     l1 = l1.next
        #     l2 = l2.next
        # return head.next

        mul = 1
        num1, num2 = 0, 0
        while l1 != None:
            num1 += (mul*l1.val)
            mul *= 10
            l1 = l1.next
        mul = 1
        while l2 != None:
            num2 += (mul*l2.val)
            mul *= 10
            l2 = l2.next
        score = num1 + num2

        head = tmp = ListNode()

        while score > 0:
            tmp.next = score % 10
            tmp = tmp.next
            score = score // 10
        return head.next
