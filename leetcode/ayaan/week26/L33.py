class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid
        k = start
        nums = nums[k:] + nums[:k]
        print(nums)

        start = 0
        end = len(nums) - 1
        result = -1

        while start <= end:
            mid = (start + end) // 2
            if target < nums[mid]:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                return (mid + k) % len(nums)
        return -1
