from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = 0

        for num in nums:
            temp = int(temp) ^ num

        return int(temp)
