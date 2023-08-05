class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def quick_sort(arr, start, end):
            if end - start < 1:
                return

            rand = random.randrange(start, end + 1)
            pivot = arr[rand]
            arr[end], arr[rand] = arr[rand], arr[end]

            left = start
            right = end - 1
            while True:
                while arr[left] < pivot:
                    left += 1
                while arr[right] > pivot:
                    right -= 1
                if left >= right:
                    break

                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

            arr[left], arr[end] = arr[end], arr[left]

            quick_sort(arr, start, left - 1)
            quick_sort(arr, left + 1, end)

        quick_sort(nums, 0, len(nums) - 1)
