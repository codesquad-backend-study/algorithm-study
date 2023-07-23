import heapq
from heapq import heapify
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        changed = [-i for i in nums]
        heapify(changed)

        number = 0
        for i in range(k):
            number = heapq.heappop(changed)

        return -number
