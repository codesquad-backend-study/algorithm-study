def solution(n, t, m, p):
    num_char = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    result = ''
    target_num = 0
    i = 1
    while True:
        num = target_num
        a = []
        while True:
            b = num % n
            if b > 9:
                a.append(num_char[b])
            else:
                a.append(str(b))
            if num // n == 0:
                break
            num = num // n

        target_num += 1
        cur_num = ''.join(a[::-1])

        for ch in cur_num:
            if i == p and t > 0:
                result += ch
                t -= 1
            i += 1
            if i > m:
                i = 1
        if t < 1:
            break

    return result
