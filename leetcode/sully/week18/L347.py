import collections
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = []

        counter = collections.Counter(nums)
        tmp = counter.most_common(k)
        for t in tmp:
            answer.append(t[0])

        return answer
