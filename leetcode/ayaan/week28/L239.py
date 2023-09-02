def maxSlidingWindow(nums, k):
    if k == 1:
        return nums
    answer = [max(nums[:k])]
    max_num = max(nums[:k])
    for i in range(1, len(nums) - k + 1):
        if max_num > nums[i - 1]:
            max_num = max(max_num, nums[i+k-1])
        else:
            max_num = max(nums[i:i + k])
        answer.append(max_num)
    return answer

result = maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
print(result)
