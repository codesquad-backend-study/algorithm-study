class Solution:
    def search(self, nums: List[int], target: int) -> int:

        start = 0
        end = len(nums) - 1
        mid = (end + start) // 2

        while end - start >= 0:
            if nums[mid] < target:
                start = mid + 1
                end = end

            elif nums[mid] > target:
                start = start
                end = mid - 1

            elif nums[mid] == target:
                return mid

            mid = (end + start) // 2

        return -1
