from typing import List


def search(nums: List[int], target: int) -> int:
    target_index = [-1]

    def function(start, end):
        if start > end or start < 0 or end > len(nums):
            return
        mid = (start + end) // 2
        if mid >= len(nums) or mid < 0:
            return
        if nums[mid] < target:
            function(mid + 1, end)
        elif nums[mid] > target:
            function(start, mid - 1)
        elif nums[mid] == target:
            target_index[0] = mid

    function(0, len(nums))

search([-1,0,3,5,9,12], 13)
