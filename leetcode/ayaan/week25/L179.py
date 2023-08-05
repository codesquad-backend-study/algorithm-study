class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(1, len(nums)):
            j = i
            pivot = nums[i]
            while j > 0 and int(str(pivot) + str(nums[j - 1])) > int(str(nums[j - 1]) + str(pivot)):
                nums[j] = nums[j - 1]
                j -= 1
            nums[j] = pivot
        return str(int(''.join(list(map(str, nums)))))
