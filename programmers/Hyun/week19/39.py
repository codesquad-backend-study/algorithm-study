class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()

        def dfs(chunk, sum_value, cur_idx):
            if sum_value == target:
                ans.add(tuple(chunk))
                return

            for idx, i in enumerate(candidates[cur_idx:]):
                if sum_value + i <= target:
                    dfs(chunk + [i], sum_value + i, cur_idx + idx)

        for idx, each in enumerate(candidates):
            dfs([each], each, idx)

        return ans
