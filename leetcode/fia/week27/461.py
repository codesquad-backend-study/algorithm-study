class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        number = bin(x ^ y)

        count = 0
        for char in number[2:]:
            if char == '1':
                count += 1

        return count
