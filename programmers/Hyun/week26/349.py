class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        targets = set(nums2)

        def find(target: int):
            start = 0
            end = len(nums1) - 1

            while start <= end:
                mid = (start + end) // 2

                if nums1[mid] < target:
                    start = mid + 1

                elif nums1[mid] > target:
                    end = mid - 1

                elif nums1[mid] == target:
                    return True

            return False

        ans = []
        for target in targets:
            if find(target):
                ans.append(target)

        return ans
