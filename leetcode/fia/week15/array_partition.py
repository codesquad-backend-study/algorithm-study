from typing import List


def arrayPairSum(nums: List[int]) -> int:
    nums.sort()
    answer = 0
    for index in range(0, len(nums), 2):
        answer += nums[index]

    return answer
