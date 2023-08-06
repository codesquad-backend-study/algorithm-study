from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Follow up: Could you come up with a one-pass algorithm using only constant extra space?
        """
        # Red, White, Blue 순서 (0, 1, 2)
        # start = red, mid = white, end = blue
        start, mid, end = 0, 0, len(nums) - 1

        while mid <= end:
            # mid가 start쪽에 있을 때
            if nums[mid] == 0:
                nums[start], nums[mid] = nums[mid], nums[start]
                start += 1
                mid += 1
                continue

            # mid가 자기 자신쪽에 있을 때
            if nums[mid] == 1:
                mid += 1
                continue

            # mid가 end쪽에 있을 때
            if nums[mid] == 2:
                nums[mid], nums[end] = nums[end], nums[mid]
                end -= 1
