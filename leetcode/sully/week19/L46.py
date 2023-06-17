from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def dfs(elements: List[int]) -> None:

            if len(elements) == len(nums):
                answer.append(elements[:])
                return

            for num in nums:
                if num not in elements:
                    elements.append(num)
                    dfs(elements)
                    elements.pop()

        for i in range(len(nums)):
            dfs([nums[i]])

        return answer
