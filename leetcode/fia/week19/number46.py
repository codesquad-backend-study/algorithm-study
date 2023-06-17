class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        check = [False] * len(nums)

        def func(index, path):
            if len(path) == len(nums):
                answer.append(path[:])
                return

            check[index] = True

            for inde, number in enumerate(nums):
                if not check[inde]:
                    path.append(number)
                    func(inde, path)
                    path.pop()
            check[index] = False

        for index, number in enumerate(nums):
            func(index, [number])

        return answer
