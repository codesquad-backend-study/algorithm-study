import heapq
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = []
        # 슬라이싱 윈도우 값들을 저장
        max_heap = []

        for i, num in enumerate(nums):
            # 힙에서 가장 큰 값이 루트에 위치하게 됨
            heapq.heappush(max_heap, (-num, i))

            if i >= k - 1:
                current_i = max_heap[0][1]
                # 윈도우를 이동하면서 윈도우에서 벗어나는 값은 힙에서 제거
                while current_i < i - k + 1:
                    heapq.heappop(max_heap)

                # 힙의 루트에 있는 값이 현재 윈도우 내의 최대값이 됨
                current_num = max_heap[0][0]
                answer.append(-current_num)

        return answer
