from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def dfs(index: int, elements: List[int]) -> None:
            answer.append(elements)

            for i in range(index, len(nums)):
                dfs(i + 1, elements + [nums[i]])

        dfs(0, [])

        return answer
