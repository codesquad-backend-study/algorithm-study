class Solution:
    def getSum(self, a: int, b: int) -> int:
        or_operator = a | b
        and_operator = a & b
        xor_operator = or_operator ^ and_operator
        shift_operator = and_operator << 1

        return ((xor_operator & shift_operator) << 1) | (xor_operator ^ shift_operator)





