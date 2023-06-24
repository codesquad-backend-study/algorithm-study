class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def combi(number, path, current, sum_value):
            if sum_value == target:
                answer.append(path[:])
                return

            for index, num in enumerate(candidates[current:]):
                if sum_value + num <= target:
                    path.append(num)
                    combi(num, path, index + current, sum_value + num)
                    path.pop()

        for index, candidate in enumerate(candidates):
            combi(candidate, [candidate], index, candidate)

        return answer
