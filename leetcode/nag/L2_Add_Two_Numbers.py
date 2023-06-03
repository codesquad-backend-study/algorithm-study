class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        overTen = False
        list = []
        index = 0
        while l1 and l2:
            sum = l1.val + l2.val + 1 if overTen else l1.val + l2.val
            list.append(sum % 10)
            overTen = True if sum >= 10 else False
            l1, l2 = l1.next, l2.next
        if l1:
            while l1:
                sum = l1.val + 1 if overTen else l1.val
                list.append(sum % 10)
                overTen = True if sum >= 10 else False
                l1 = l1.next
        else:
            while l2:
                sum = l2.val + 1 if overTen else l2.val
                list.append(sum % 10)
                overTen = True if sum >= 10 else False
                l2 = l2.next
        if overTen:
            list.append(1)       
        answer = ListNode()
        head = answer
        for index in range(len(list) - 1):
            head.val = list[index]
            head.next = ListNode()
            head = head.next
        head.val = list[-1]
        return answer
