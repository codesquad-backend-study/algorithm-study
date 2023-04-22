import re

def solution(expression):
    ops = ["*+-", "*-+", "-*+", "-+*", "+*-", "+-*"]
    exp = re.findall(r'[^0-9]|[0-9]+', expression)
    ans = 0

    for op in ops:
        post_exp = []                               # 중위 표기식 -> 후위 표기식 변환
        op_stack = []
        for ch in exp:
            if ch == op[2]:
                while op_stack and op_stack[-1] in [op[0], op[1], op[2]]:
                    post_exp.append(op_stack.pop())
                op_stack.append(ch)
            elif ch == op[1]:
                while op_stack and op_stack[-1] in [op[0], op[1]]:
                    post_exp.append(op_stack.pop())
                op_stack.append(ch)
            elif ch == op[0]:
                while op_stack and op_stack[-1] == op[0]:
                    post_exp.append(op_stack.pop())
                op_stack.append(ch)
            else:
                post_exp.append(int(ch))

        while op_stack:
            post_exp.append(op_stack.pop())


        number_stack = []
        for ch in post_exp:                                     # 후위 표기식 계산
            if ch in ["*", "-", "+"]:
                second_num = number_stack.pop()
                first_num = number_stack.pop()
                number_stack.append(calculate(first_num, second_num, ch))
            else:
                number_stack.append(ch)

        ans = max(ans, abs(number_stack.pop()))                 # 최대값 계산

    return ans


def calculate(a, b, op):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b