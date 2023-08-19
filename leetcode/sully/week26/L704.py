from typing import List


class Solution:
    # O(log n)으로 풀기
    def search(self, nums: List[int], target: int) -> int:
        lt, rt = 0, len(nums) - 1

        while lt <= rt:
            mid = (lt + rt) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                mid += lt
                lt += 1
                continue

            if nums[mid] > target:
                mid -= rt
                rt -= 1

        return -1
