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
    def quick_sort(lo, hi):
        # 탈출 조건
        if lo >= hi:
            return

        start = lo
        end = hi
        # pivot : 중간값
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

        # lo가 나누는 기준이 됨
        # lo의 왼쪽
        quick_sort(start, lo - 1)
        # lo부터 끝까지
        quick_sort(lo, end)

    quick_sort(0, len(nums) - 1)
