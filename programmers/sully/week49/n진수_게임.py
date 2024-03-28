def solution(n, t, m, p):
    answer = ''
    converted = ''

    idx = p - 1
    for num in range(t * m):
        converted += convert(num, n)

    while True:
        if len(answer) == t:
            break

        answer += converted[idx]
        idx += m

    return answer


def convert(num, n):
    if num == 0:
        return '0'

    numbers = '0123456789ABCDEF'
    tmp = ''
    while num > 0:
        num, mod = divmod(num, n)
        tmp += numbers[mod]

    return tmp[::-1]


print(solution(2, 4, 2, 1))
