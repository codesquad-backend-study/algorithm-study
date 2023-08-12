class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        if len(nums) == 1:
            return -1 if nums[0] != target else 0

        while left <= right:
            mid = left + (right - left) // 2

            if target == nums[mid]:
                return mid

            l_left = left
            l_right = mid - 1
            if l_right < 0:
                l_right = left

            r_left = mid + 1
            r_right = right
            if r_left > len(nums) - 1:
                r_left = r_right

            if nums[r_left] > nums[mid] and nums[r_right] > nums[mid]:
                if min(nums[r_left], nums[r_right]) <= target <= max(nums[r_left], nums[r_right]):
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if min(nums[l_left], nums[l_right]) <= target <= max(nums[l_left], nums[l_right]):
                    right = mid - 1
                else:
                    left = mid + 1

        return -1


