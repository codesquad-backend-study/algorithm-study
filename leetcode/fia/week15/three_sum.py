from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    triplets = set()
    nums.sort()

    def two_pointer(target: int, start: int):
        left_index = start
        right_index = len(nums) - 1

        while left_index < right_index:
            if nums[left_index] + nums[right_index] + target > 0:
                right_index -= 1
            elif nums[left_index] + nums[right_index] + target < 0:
                left_index += 1
            else:
                triplets.add((target, nums[left_index], nums[right_index]))
                right_index -= 1
                left_index += 1

    for i in range(len(nums)):
        target_number = nums[i]
        two_pointer(target_number, i + 1)

    return list(triplets)
