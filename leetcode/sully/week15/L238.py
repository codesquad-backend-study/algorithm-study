from typing import List


class Solution:
    # 나누기 연산 쓰지 말고, O(N)으로
    # 나누기 쓸 수 있으면 sum(nums)한 다음에 하나씩 나눠주면 끝이긴 함
    # 결국 나누기를 사용하지 못 하니까 자신을 제외한 곱셈들을 이용하는 방법밖에 없음
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []

        # 왼쪽부터 곱한 결과를 answer 배열에 저장
        times = 1
        for num in nums:
            answer.append(times)
            times *= num

        times = 1
        # 왼쪽부터 곱한 결과에 오른쪽 값들을 차례대로 곱해서 저장하자
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= times
            times *= nums[i]

        return answer
