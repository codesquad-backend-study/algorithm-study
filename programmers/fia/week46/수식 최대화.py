import re
from collections import deque


def solution(expression):
    groups = [("*", "+", "-"),
              ("*", "-", "+"),
              ("+", "*", "-"),
              ("+", "-", "*"),
              ("-", "+", "*"),
              ("-", "*", "+")]

    answer = 0

    for group in groups:
        queue = deque(re.findall('[\d]+|[-+*]', expression))
        stack = []

        for operation in group:
            while queue:
                current = queue.popleft()

                if current == operation:
                    if operation == '-':
                        stack.append(int(stack.pop()) - int(queue.popleft()))
                    elif operation == '+':
                        stack.append(int(stack.pop()) + int(queue.popleft()))
                    else:
                        stack.append(int(stack.pop()) * int(queue.popleft()))
                else:
                    stack.append(current)

            queue = deque(stack)
            stack = []

        answer = max(answer, abs(queue[0]))

    return answer
