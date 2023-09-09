class Solution:
    def climbStairs(self, n: int) -> int:
        d = [[0] * 2 for _ in range(n + 3)]

        d[1][0] = 1
        d[1][1] = 0

        d[2][0] = 1
        d[2][1] = 1

        for i in range(3, n + 1):
            d[i][0] = sum(d[i - 1])
            d[i][1] = sum(d[i - 2])

        return sum(d[n])
