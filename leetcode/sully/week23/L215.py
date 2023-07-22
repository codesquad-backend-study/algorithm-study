import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        answer = 0

        heap = []
        for num in nums:
            heapq.heappush(heap, -num)

        for _ in range(k):
            answer = -heapq.heappop(heap)

        return answer
