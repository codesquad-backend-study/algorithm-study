class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)

        ans = []
        for val, _ in counter.most_common(k):
            ans.append(val)
        return ans
