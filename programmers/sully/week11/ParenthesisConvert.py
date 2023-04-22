def divide(p):
    if p == '':
        return ''

    left, right = 0, 0
    u, v = 0, 0
    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1

        if left == right:
            u, v = p[:i + 1], p[i + 1:]
            break

    if is_right(u):
        return u + divide(v)
    else:
        tmp = '('
        tmp += divide(v)
        tmp += ')'

        u = u[1:-1]
        for w in u:
            if w == '(':
                tmp += ')'
            else:
                tmp += '('

        return tmp


def is_right(p):
    cnt = 0

    for w in p:
        if w == '(':
            cnt += 1
        else:
            cnt -= 1

        if cnt < 0:
            return False

    if cnt == 0:
        return True
    else:
        return False


def solution(p):
    answer = divide(p)
    return answer
