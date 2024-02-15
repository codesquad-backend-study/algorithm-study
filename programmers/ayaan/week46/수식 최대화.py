from collections import deque
import itertools


def solution(expression):
    answer = 0
    ops = ['*', '-', '+']

    number = ''
    exp = []
    for ch in expression:
        if ch in ['*', '-', '+']:
            exp.append(number)
            exp.append(ch)
            number = ''
        else:
            number += ch
    exp.append(number)

    for op in ops:
        if op not in exp:
            ops.remove(op)

    cases = itertools.permutations(ops)

    for case in cases:
        dq = deque(exp)
        for op in case:
            stack = []
            while dq:
                item = dq.popleft()
                if item == op:
                    a = stack.pop()
                    b = dq.popleft()
                    stack.append(str(eval(a + item + b)))
                else:
                    stack.append(item)
            dq = deque(stack)
        answer = max(answer, abs(int(dq[0])))

    return answer


solution('100-200*300-500+20')
