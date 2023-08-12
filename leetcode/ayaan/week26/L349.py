class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        def binary_search(nums, target):
            start = 0
            end = len(nums) - 1
            mid = (start + end) // 2

            while start <= end:
                if target < nums[mid]:
                    end = mid - 1
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    return True
                mid = (start + end) // 2
            return False

        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        answer = []
        if len(nums1) < len(nums2):
            nums2.sort()
            for num in nums1:
                if binary_search(nums2, num):
                    answer.append(num)
        else:
            nums1.sort()
            for num in nums2:
                if binary_search(nums1, num):
                    answer.append(num)
        print(answer)
        return answer
