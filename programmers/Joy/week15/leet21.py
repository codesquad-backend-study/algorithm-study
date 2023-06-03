answer = tmp = ListNode()

while True:
    if not list1 and not list2:
        break
    if not list1:
        answer.next = list2
        answer = answer.next
        list2 = list2.next
        continue
    if not list2:
        answer.next = list1
        answer = answer.next
        list1 = list1.next
        continue

    if list1.val >= list2.val:
        answer.next = list2
        answer = answer.next
        list2 = list2.next
    else:
        answer.next = list1
        answer = answer.next
        list1 = list1.next

return tmp.next