class Solution:
    max_size = 0
    nums = []
    visit = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.max_size = len(nums)
        self.visit = [False] * self.max_size

        ans = []
        for idx, num in enumerate(nums):
            self.dfs(idx, [num], ans)

        return ans

    def dfs(self, cur_idx, chunk, ans):
        if len(chunk) >= self.max_size:
            ans.append(chunk)
            return

        self.visit[cur_idx] = True

        for idx, num in enumerate(self.nums):
            if not self.visit[idx]:
                self.dfs(idx, chunk + [self.nums[idx]], ans)

        self.visit[cur_idx] = False
