class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)

        stack = []
        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                peek = stack.pop()
                ans[peek[0]] = idx - peek[0]

            stack.append((idx, temp))

        return ans
