from typing import List


class Solution:
    # 삽입 정렬 문제
    # 가장 큰 수를 만들어서 문자열로 반환
    def largestNumber(self, nums: List[int]) -> str:
        # 앞자리가 가장 큰 수로 정렬, 그 다음에는 그 다음 숫자들로 정렬
        # 삽입 정렬도 스왑 이용하면 될 듯?
        for i in range(len(nums)):
            # Discusstion:
            # The solution of the problem rests on observing that if AB > BA.
            # Then we have ACB > BCA for any C.
            for j in range(i, 0, -1):
                if int(str(nums[j - 1]) + str(nums[j])) < int(str(nums[j]) + str(nums[j - 1])):
                    nums[j - 1], nums[j] = nums[j], nums[j - 1]
                    continue

                break

        return str(int(''.join(list(map(str, nums)))))
