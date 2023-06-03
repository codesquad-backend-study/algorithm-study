def reverse_linked_list(head: ListNode) -> ListNode:
    current = head
    reverse = None

    while current:
        temp = current.next
        current.next = reverse
        reverse = current
        current = temp

    return reverse
