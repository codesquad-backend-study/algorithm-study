def maxProfit(self, prices: List[int]) -> int:
    answer = 0
    buy = prices[0]
    prev = buy
    profit = 0
    for i in range(len(prices) - 1):
        if prev > prices[i + 1]:
            answer += profit
            profit = 0
            prev = prices[i + 1]
            buy = prev
            continue
        elif prev < prices[i + 1]:
            profit = prices[i + 1] - buy
            prev = prices[i + 1]
    answer += profit
    return answer
