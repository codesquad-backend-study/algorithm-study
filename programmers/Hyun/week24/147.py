# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return

        def insertion_sort(arr):
            for i in range(1, len(arr)):
                j = i
                pivot = arr[i]
                while j > 0 and pivot < arr[j - 1]:
                    arr[j] = arr[j - 1]
                    j -= 1

                arr[j] = pivot

        numbers = []

        while head:
            numbers.append(head.val)
            head = head.next

        insertion_sort(numbers)

        head = ListNode(numbers[0])
        current = head
        for number in numbers[1:]:
            current.next = ListNode(number)
            current = current.next

        return head
