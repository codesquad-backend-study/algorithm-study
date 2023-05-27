from typing import List


class Solution:
    # min()을 한 결과값들의 합이 최대가 되도록 하는 문제
    # (가장 작은 수, 가장 큰 수) -> 이렇게 최소가 되도록 하려면 두 수의 차이가 최대한 커야 되잖아?
    # 그니까 최대가 되도록 하려면 두 수의 차이가 거의 없도록 해야 될 거 같음
    # 단, 예제 1처럼 모든 수의 차가 같은 경우를 봤을 때 오름차순 순서대로 하는 게 정답임. 그러므로 정렬해 주자
    def arrayPairSum(self, nums: List[int]) -> int:
        # 1) [1, 2, 3, 4]
        # 2) [1, 2, 2, 5, 6, 6]
        answer = 0

        # 위에서 설명한 대로 오름차순 정렬
        nums.sort()

        for i in range(0, len(nums), +2):
            answer += nums[i]

        return answer
