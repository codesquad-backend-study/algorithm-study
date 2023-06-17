class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def func(path):
            if len(path) == len(nums):
                answer.append(path[:])
                return

            for number in nums:
                if number not in path:
                    path.append(number)
                    func(path)
                    path.pop()

        for number in nums:
            func([number])

        return answer
