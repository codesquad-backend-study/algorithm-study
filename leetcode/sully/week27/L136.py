from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0

        for num in sorted(nums):
            # answer에 num 값을 계속 저장하는데, "^"을 사용하여 중복된 값이 저장되지 않게 함
            # 만약 [2(1), 2(2), 1]이라고 했을 때,
            # 2(1) 이미 저장되어 있으면 2(1)과 2(1)의 "^" 연산은 0이 됨
            # 즉, 최종적으로 중복되지 않는 값이 저장되는 거지

            # 단, 위 모든 것들은 이미 nums가 정렬되어 있다는 전제 하에 일어나야 함
            answer = answer ^ num

        return answer
