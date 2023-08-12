class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def correct_nums():
            start = 0
            end = len(nums) - 1
            mid = (start + end) // 2
            fivot = nums[mid]

            while not (nums[start] <= nums[mid] <= nums[end]):
                if nums[start] > nums[mid]:
                    end = mid - 1

                elif nums[mid] > nums[end]:
                    start = mid + 1

                mid = (start + end) // 2

            if nums[start] < fivot:
                return nums[start:] + nums[:start], start

            else:
                return nums[end + 1:] + nums[:end + 1], end + 1

        nums, offset = correct_nums()

        print(nums, offset)

        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] > target:
                end = mid - 1

            elif nums[mid] < target:
                start = mid + 1

            elif nums[mid] == target:
                return (offset + mid) % len(nums)

        return -1
