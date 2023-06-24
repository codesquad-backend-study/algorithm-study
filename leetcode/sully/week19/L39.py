from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def dfs(index: int, _sum: int, elements: List[int]) -> None:
            if _sum > target:
                return

            # 백트래킹
            if _sum == target:
                answer.append(elements[:])
                return

            for i in range(index, len(candidates)):
                dfs(i, _sum + candidates[i], elements + [candidates[i]])

        dfs(0, 0, [])

        return answer
