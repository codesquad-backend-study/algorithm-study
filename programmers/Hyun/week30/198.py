class Solution:
    def rob(self, nums: List[int]) -> int:
        d = [[0] * 2 for _ in range(len(nums))]

        d[0][0] = 0
        d[0][1] = nums[0]

        for i in range(1, len(nums)):
            d[i][0] = max(d[i - 1])
            d[i][1] = d[i - 1][0] + nums[i]

        return max(d[-1])
