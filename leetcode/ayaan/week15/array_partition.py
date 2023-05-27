def array_pair_sum(nums):
    nums.sort()
    result = 0
    i = 0
    while i <= len(nums)-1:
        result += min(nums[i:i+2])
        i += 2
    print(result)
    return result

array_pair_sum([1,4,3,2])
