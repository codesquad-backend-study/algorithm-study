class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        numbers = [i for i in range(1, n + 1)]
        max_size = k
        visit = [False] * len(numbers)
        ans = set()

        def dfs(cur_idx, chunk):
            if len(chunk) >= max_size:
                ans.add(tuple(chunk))
                return

            visit[cur_idx] = True

            for number in numbers[cur_idx + 1:]:
                if not visit[number - 1]:
                    dfs(number - 1, chunk + [numbers[number - 1]])

            visit[cur_idx] = False

        for num in numbers:
            dfs(num - 1, [num])

        return ans
