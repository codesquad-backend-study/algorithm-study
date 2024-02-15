# +, -, * 우선순위 정하기
import itertools
import re


def solution(expression: str) -> int:
    answer = set()

    all_cases = list(itertools.permutations({'-', '+', '*'}, 3))
    expression = re.split('([-+*])', expression)

    for case in all_cases:
        current_expression = expression[:]

        for current_op in case:
            while current_op in current_expression:
                current_idx = current_expression.index(current_op)
                current_expression[current_idx - 1] = str(
                    eval(current_expression[current_idx - 1] + current_op + current_expression[current_idx + 1])
                )
                del current_expression[current_idx: current_idx + 2]

        answer.add(abs(int(current_expression[0])))

    return max(answer)


print(solution("100-200*300-500+20"))
