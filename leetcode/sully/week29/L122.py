from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0

        for i in range(len(prices) - 1):
            current, next = prices[i], prices[i + 1]
            if current < next:
                answer += next - current

        return answer
