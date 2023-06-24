def permute(self, nums: List[int]) -> List[List[int]]:
    def dfs(permu):
        if len(permu) == len(nums):
            result.append(permu)
            return
        for i in range(len(nums)):
            if nums[i] not in permu:
                permu.append(nums[i])
                dfs(permu[:])
                permu.pop()

    result = []
    for i in range(len(nums)):
        dfs([nums[i]])
    return result
