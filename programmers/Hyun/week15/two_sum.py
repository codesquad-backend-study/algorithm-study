class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if target == nums[i] + nums[j]:
                    return [i, j]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums = [(num, idx) for idx, num in enumerate(nums)]

        sorted_nums = sorted(nums, key=lambda x: x[0])

        front = 0
        rear = len(sorted_nums) - 1

        while front < rear:
            if target > sorted_nums[front][0] + sorted_nums[rear][0]:
                front += 1
            elif target < sorted_nums[front][0] + sorted_nums[rear][0]:
                rear -= 1
            else:
                return [sorted_nums[front][1], sorted_nums[rear][1]]


