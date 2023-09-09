import collections


class Solution:

    dp = collections.defaultdict(int)

    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        if self.dp[n]:
            return self.dp[n]

        # 계산한 값을 딕셔너리에 저장해둠
        self.dp[n] = self.fib(n - 1) + self.fib(n - 2)

        return self.dp[n]
