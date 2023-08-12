from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = set()

        for n1 in nums1:
            for n2 in nums2:
                if n1 == n2:
                    answer.add(n1)

        return list(answer)
