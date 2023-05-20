from typing import List


class Solution:
    # 현재에 주식을 매수하고, 미래에 주식을 매도한다. -> 이 최댓값 구하는 문제
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0

        min_price = prices[0]
        for cur_price in prices:
            # 시간은 미래로만 흘러가는 것이니, 현재에서 과거의 최대를 계속 빼나가다 보면 결국 최대가 도출되게 됨
            answer = max(cur_price - min_price, answer)
            min_price = min(cur_price, min_price)
            
        return answer
