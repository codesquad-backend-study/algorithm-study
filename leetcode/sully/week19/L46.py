from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        visited = [False] * len(nums)

        def dfs(index: int, elements: List[int]) -> None:
            if len(elements) == len(nums):
                answer.append(elements[:])
                return

            visited[index] = True

            for j, n in enumerate(nums):
                if not visited[j]:
                    elements.append(n)
                    dfs(j, elements)
                    elements.pop()

            visited[index] = False

        for i, num in enumerate(nums):
            dfs(i, [num])

        return answer
