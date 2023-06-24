class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = [[]]

        def dfs(current_idx, subset, size):
            if size <= len(subset):
                ans.append(subset)
                return

            for idx, number in enumerate(nums[current_idx + 1:]):
                dfs(idx + current_idx + 1, subset + [number], size)

        for size in range(1, len(nums) + 1):
            for start in range(len(nums)):
                dfs(start, [nums[start]], size)

        return ans


