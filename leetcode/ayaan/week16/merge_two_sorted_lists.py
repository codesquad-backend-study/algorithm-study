def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1 and not list2:
        return None

    list1_list = []
    list2_list = []

    while list1 != None:
        list1_list.append(list1.val)
        list1 = list1.next
    while list2 != None:
        list2_list.append(list2.val)
        list2 = list2.next

    merge = list1_list + list2_list
    merge.sort()

    result = ListNode(merge[0])
    temp = result
    for i in range(1, len(merge)):
        temp.next = ListNode(merge[i])
        temp = temp.next
    return result
