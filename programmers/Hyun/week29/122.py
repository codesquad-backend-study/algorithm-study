class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        d = [0] * len(prices)

        for i in range(1, len(prices)):
            d[i] = d[i - 1] + max(0, prices[i] - prices[i - 1])

        return max(d)
