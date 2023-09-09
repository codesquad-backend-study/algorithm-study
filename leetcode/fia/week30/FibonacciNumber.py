class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        numbers = [0] * n
        numbers[1] = 1

        for index in range(2, n):
            numbers[index] = numbers[index - 1] + numbers[index - 2]

        return numbers[-1] + numbers[-2]
