import collections


def getSum(a, b):
    carry = 0
    number = collections.deque([])
    while a != 0 or b != 0:
        a_plus_b = a % 2 ^ b % 2
        carry = a_plus_b & carry

        number.appendleft(a_plus_b ^ carry)
        carry = (a % 2 & b % 2) | carry

        a //= 2
        b //= 2
    if carry:
        number.appendleft(carry)
    print(int(''.join(map(str, number)), 2))
    return int(''.join(map(str, number)), 2)

getSum(10, 11)
