from typing import List


class Solution:
    # @return 2개의 정답 index에서 +1을 한 두 값을 저장하는 배열
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        lt, rt = 0, len(numbers) - 1
        while lt <= rt:
            sum_ = numbers[lt] + numbers[rt]

            if sum_ == target:
                return [lt + 1, rt + 1]

            if sum_ < target:
                lt += 1
                continue

            if sum_ > target:
                rt -= 1

        return []
