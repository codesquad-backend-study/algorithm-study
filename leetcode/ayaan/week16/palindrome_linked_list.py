def isPalindrome(self, head: Optional[ListNode]) -> bool:
    node_list = []
    while head != None:
        node_list.append(head.val)
        head = head.next

    if node_list == node_list[::-1]:
        return True
    return False
