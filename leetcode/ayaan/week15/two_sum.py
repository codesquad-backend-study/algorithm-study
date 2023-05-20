def twoSum(nums, target):
    nums_map = {}
    for i, num in enumerate(nums):
        nums_map[num] = i
    print(nums_map)
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            print([i, nums_map[target - num]])
            return [i, nums_map[target - num]]


twoSum([3,2,4], 6)
