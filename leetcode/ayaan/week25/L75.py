def sortColors(self, nums: List[int]) -> None:
    """
    삽입 정렬
    """
    for i in range(1, len(nums)):
        target = nums[i]
        j = i
        while j > 0 and nums[j - 1] > target:
            nums[j] = nums[j - 1]
            j -= 1
        nums[j] = target
    # [9, 4, -80, 1, 172, 13, 9, 39, -99, 2054, 10, -10, 3, 67, -28]


    """
    퀵 정렬
    """
    def sort(lo, hi):
        if lo >= hi:
            return

        mid = partition(lo, hi)
        sort(lo, mid - 1)
        sort(mid, hi)

    def partition(lo, hi):
        pivot = nums[(lo + hi) // 2]
        while lo <= hi:
            while nums[lo] < pivot:
                lo += 1
            while nums[hi] > pivot:
                hi -= 1
            if lo <= hi:
                nums[lo], nums[hi] = nums[hi], nums[lo]
                lo += 1
                hi -= 1
        return lo

    sort(0, len(nums) - 1)
