def findKthLargest(self, nums: List[int], k: int) -> int:
    heapq._heapify_max(nums)
    result = 0
    for _ in range(k):
        result = heapq._heappop_max(nums)

    return result

def findKthLargest2(self, nums: List[int], k: int) -> int:
    hq = []
    for num in nums:
        heapq.heappush(hq, (-num, num))

    result = 0
    for _ in range(k):
        result = heapq.heappop(hq)[1]

    return result
