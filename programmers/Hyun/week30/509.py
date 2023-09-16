class Solution:
    def fib(self, n: int) -> int:
        d = [0] * 32

        d[0] = 0
        d[1] = 1

        for i in range(2, n + 1):
            d[i] = d[i - 2] + d[i - 1]

        return d[n]
