from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    answer = []
    for i, number in enumerate(nums):
        if target - number in nums[i + 1:]:
            answer.append(i)
            answer.append(nums[i + 1:].index(target - number) + i + 1)
            return answer

    return answer

