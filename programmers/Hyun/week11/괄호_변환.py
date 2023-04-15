def solution(p):
    return find_v(p)


def find_v(string):                 # 로직이 이해 안돼도, 슈도코드대로 하면 되더라..
    left_cnt = 0
    right_cnt = 0

    if not string:
        return ""

    for idx, ch in enumerate(string):
        if ch == "(":
            left_cnt += 1
        else:
            right_cnt += 1

        if left_cnt == right_cnt:
            if check(string[:idx + 1]):
                return string[:idx + 1] + find_v(string[idx + 1:])
            else:
                return "(" + find_v(string[idx + 1:]) + ")" + reverse_parenthesis(string[:idx + 1])


def check(string):                          # 올바른 괄호 문자열인지 체크
    stack = []

    for ch in string:
        if ch == "(":
            stack.append(1)
        elif ch == ")" and not stack:
            return False
        else:
            stack.pop()

    if stack:
        return False

    return True


def reverse_parenthesis(string):            # u 의 앞뒤는 자르고, 괄호 전부 뒤집기
    processed = list(string[1:-1])

    for idx in range(len(processed)):
        if processed[idx] == ")":
            processed[idx] = "("
        else:
            processed[idx] = ")"

    return ''.join(processed)