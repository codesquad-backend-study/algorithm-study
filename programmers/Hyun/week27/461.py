class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        num = x ^ y
        cnt = 0

        while num > 0:
            if num % 2 == 1:
                cnt += 1
            num //= 2

        return cnt
