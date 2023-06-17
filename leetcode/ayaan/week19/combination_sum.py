def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    result = []

    def dfs(idx, combi):
        if sum(combi) == target:
            result.append(combi)
            return

        for i in range(idx, len(candidates)):
            combi.append(candidates[i])
            if sum(combi) > target:
                combi.pop()
                continue
            dfs(i, combi[:])
            combi.pop()

    for i, num in enumerate(candidates):
        dfs(i, [num])

    return result
