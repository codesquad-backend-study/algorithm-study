from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 1. Brute Force - O(n^2)
        answer = set()

        for n1 in nums1:
            for n2 in nums2:
                if n1 == n2:
                    answer.add(n1)

        return list(answer)

        # 2. Hash Table - O(N)
        answer = set()

        num1_dic = {n1 for n1 in nums1}
        for n2 in nums2:
            if n2 in num1_dic:
                answer.add(n2)

        return answer
