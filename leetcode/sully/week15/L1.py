import collections
from typing import List


class Solution:
    # 두 num을 더해서 target이 되는 그 num의 i(index) 값을 배열로 리턴
    # num[i] + num[j] = target -> num[i] = target - num[j]
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = collections.defaultdict(int)

        # dic[value] = index 형식
        for i, num in enumerate(nums):
            if target - num in dic:
                return [dic[target - num], i]

            dic[num] = i

