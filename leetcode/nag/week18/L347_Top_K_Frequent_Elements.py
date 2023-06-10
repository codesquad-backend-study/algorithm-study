class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}

        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
        answer = []
        for i in range(k):
            answer.append(dict[i][0])
        return answer
