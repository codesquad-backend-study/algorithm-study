from typing import List


class Solution:
    # 3개 더해서 0이 되는 경우의 배열을 계속 append
    # 완전 탐색으로 하려면 n^3 될 거 같은데 투포인터로 한번 n^2 만들어 보자
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []

        # 구현하기 편하도록 오른차순 정렬해 두자
        nums.sort()

        # 일단 이 반복문이 전체 뼈대를 잡아줄 수 있도록 하자
        for i, num in enumerate(nums):
            # nums[i]를 중심으로 [i + 1 : -1]까지의 원소들을 투포인터로 각각 비교하는 방법 시도해 보자
            lt, rt = i + 1, len(nums) - 1
            # 이렇게 하면 n^3으로 풀 수밖에 없을 거 같은데 흠..
            while lt < rt:
                # 이제 lt는 가만히 있고, rt가 또 한 번의 반복문 돌아주면서 lt 바로 전까지 rt -= 1을 해주면 되긴 할 듯

                if num + nums[lt] + nums[rt] == 0:
                    answer.append([num, nums[lt], nums[rt]])

        return answer
