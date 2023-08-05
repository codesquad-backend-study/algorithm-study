class Solution:
    def sortColors(self, nums: List[int]) -> None:
        def quick_sort(nums, left, right):
            if left >= right:
                return

            pivot = partitioning(nums, left, right)
            quick_sort(nums, left, pivot - 1)
            quick_sort(nums, pivot + 1, right)

        def partitioning(nums, left, right):
            l = left
            r = right
            pivot = nums[right]

            while l < r:
                while nums[l] < pivot and l < r:
                    l += 1

                while nums[r] >= pivot and l < r:
                    r -= 1

                nums[l], nums[r] = nums[r], nums[l]

            nums[right], nums[r] = nums[r], nums[right]

            return r

        quick_sort(nums, 0, len(nums) - 1)
