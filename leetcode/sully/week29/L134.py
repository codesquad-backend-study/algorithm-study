from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        answer = 0

        if sum(gas) < sum(cost):
            return -1

        current_gas = 0
        for i in range(len(gas)):
            if gas[i] + current_gas < cost[i]:
                # 이 if문에서는 현재 위치에서 출발할 수 없다는 의미
                # 즉, answer를 다음 index로 업데이트 후 tmp를 다시 0으로 초기화
                answer = i + 1
                current_gas = 0
                continue

            current_gas += gas[i] - cost[i]

        return answer
