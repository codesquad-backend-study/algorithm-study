class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = set()

        for idx, target in enumerate(nums):
            tail = len(nums) - 1
            head = idx + 1

            while head < tail:
                if target + nums[head] + nums[tail] > 0:
                    tail -= 1
                elif target + nums[head] + nums[tail] < 0:
                    head += 1
                else:
                    ans.add((target, nums[head], nums[tail]))
                    tail -= 1
                    head += 1

        return ans


