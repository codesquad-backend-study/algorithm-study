# 가장 큰 상금 금액 만들기
import re
import itertools


def calculate(operator, operand_1, operand_2):
    if operator == '*':
        return operand_1 * operand_2
    elif operator == '+':
        return operand_1 + operand_2
    else:
        return operand_1 - operand_2


def solution(expression):
    ans = -1
    formula = []
    number = ""
    for ch in expression:
        if ch in ['-', '+', '*']:
            formula.append(int(number))
            formula.append(ch)
            number = ""
        else:
            number += ch
    formula.append(int(number))

    for first, second, third in itertools.permutations(['-', '+', '*']):
        postfix = []
        op_stack = []
        op_rank = {first: 2, second: 1, third: 0}
        for ch in formula:
            if ch in op_rank:
                while op_stack and op_rank[ch] <= op_rank[op_stack[-1]]:
                    postfix.append(op_stack.pop())
                op_stack.append(ch)
            else:
                postfix.append(ch)
        while op_stack:
            postfix.append(op_stack.pop())

        operand_stack = []
        for ch in postfix:
            if ch in ['-', '+', '*']:
                operand_2 = operand_stack.pop()
                operand_1 = operand_stack.pop()
                result = calculate(ch, operand_1, operand_2)
                operand_stack.append(result)
            else:
                operand_stack.append(ch)

        ans = max(ans, abs(operand_stack[0]))

    return ans
