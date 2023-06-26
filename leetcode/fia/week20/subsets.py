from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    def dfs(index, path):
        answer.append(path)
        print(path)

        for i in range(index, len(nums)):
            dfs(i + 1, path + [nums[i]])

    answer = []
    dfs(0, [])

    return answer


subsets([1, 2, 3, 4])
