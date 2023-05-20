from typing import List


class Solution:
    # 3개 더해서 0이 되는 경우의 배열을 계속 append
    # 완전 탐색으로 하려면 n^3 될 거 같은데 투포인터로 한번 n^2 만들어 보자
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        set_answer = set()
        answer = []

        # 구현하기 편하도록 오른차순 정렬해 두자
        nums.sort()

        # 일단 이 반복문이 전체 뼈대를 잡아줄 수 있도록 하자
        for i, num in enumerate(nums):
            # nums[i]를 중심으로 [i + 1 : -1]까지의 원소들을 투포인터로 각각 비교하는 방법 시도해 보자
            lt, rt = i + 1, len(nums) - 1
            # 이렇게 하면 n^3으로 풀 수밖에 없을 거 같은데 흠..
            while lt < rt:
                tmp_sum = num + nums[lt] + nums[rt]

                if tmp_sum < 0:
                    lt += 1
                elif tmp_sum > 0:
                    rt -= 1
                else:
                    set_answer.add((num, nums[lt], nums[rt]))

                    lt += 1
                    rt -= 1

        return list(set_answer)


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
