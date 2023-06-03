def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    num1 = 0
    x = 1
    while l1 != None:
        num1 += l1.val * x
        x *= 10
        l1 = l1.next
    num2 = 0
    x = 1
    while l2 != None:
        num2 += l2.val * x
        x *= 10
        l2 = l2.next

    num = num1 + num2
    num_list = list(str(num))[::-1]

    result = ListNode(num_list[0])
    temp = result
    for i in range(1, len(num_list)):
        node = ListNode(num_list[i])
        temp.next(node)
        temp = temp.next
    return result
