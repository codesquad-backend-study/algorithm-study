class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        previous_max = [nums[0]]

        for num in nums[1:]:
            previous_max.append(max(previous_max[-1] + num, num))

        return max(previous_max)
