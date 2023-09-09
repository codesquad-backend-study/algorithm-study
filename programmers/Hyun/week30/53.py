class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        d = [0] * len(nums)
        d[0] = nums[0]

        for i in range(1, len(nums)):
            d[i] = max(d[i - 1] + nums[i], nums[i])

        return max(d)
