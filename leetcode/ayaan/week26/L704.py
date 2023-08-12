def search(nums, target):
    def binary_search(start, end, target):
        if start < 0 or end >= len(nums):
            return -1

        mid = (start + end) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return binary_search(mid + 1, end, target)
        else:
            return binary_search(start, mid - 1, target)

    return binary_search(0, len(nums) - 1, target)

result = search([-1,0,3,5,9,12], 9)
print(result)
