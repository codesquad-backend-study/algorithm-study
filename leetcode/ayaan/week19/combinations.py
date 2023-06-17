def combine(self, n: int, k: int) -> List[List[int]]:
    result = []
    nums = [i + 1 for i in range(n)]

    def dfs(idx, combi):
        if len(combi) == k:
            result.append(combi)
            return

        for j in range(idx, len(nums)):
            combi.append(nums[j])
            dfs(j + 1, combi[:])
            combi.pop()

    for i in range(len(nums)):
        dfs(i + 1, [nums[i]])
    return result
