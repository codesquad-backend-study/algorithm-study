class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        nums.sort()
        for i in range(0, len(nums), 2):
            if i == len(nums) - 1:
                return nums[i]
            # xor 값이 다르면 True
            elif nums[i] ^ nums[i + 1]:
                return nums[i]
