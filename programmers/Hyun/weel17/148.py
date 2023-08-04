# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return

        nodes = []

        while head:
            nodes.append(head.val)
            head = head.next

        # def quick_sort(arr, start, end):
        #     if end - start < 1:
        #         return

        #     rand = random.randrange(start, end + 1)
        #     pivot = arr[rand]
        #     arr[rand], arr[end] = arr[end], arr[rand]

        #     left = 0
        #     right = end - 1

        #     while True:
        #         while arr[left] < pivot:
        #             left += 1
        #         while arr[right] > pivot:
        #             right -= 1
        #         if left >= right:
        #             break

        #         arr[left], arr[right] = arr[right], arr[left]

        #     arr[left], arr[end] = arr[end], arr[left]

        #     quick_sort(arr, start, left - 1)
        #     quick_sort(arr, left + 1, end)

        # quick_sort(nodes, 0, len(nodes) - 1)

        def merge_sort(arr):
            if len(arr) < 2:
                return arr

            mid = len(arr) // 2
            left_arr = merge_sort(arr[:mid])
            right_arr = merge_sort(arr[mid:])

            sorted_list = []
            left = right = 0

            while left < len(left_arr) and right < len(right_arr):
                if left_arr[left] < right_arr[right]:
                    sorted_list.append(left_arr[left])
                    left += 1
                else:
                    sorted_list.append(right_arr[right])
                    right += 1

            sorted_list += left_arr[left:]
            sorted_list += right_arr[right:]
            return sorted_list

        nodes = merge_sort(nodes)

        root = ListNode(nodes[0])
        current = root

        for val in nodes[1:]:
            current.next = ListNode(val)
            current = current.next

        return root
