def solution(n, t, m, p):
    result = '0'
    while len(result) < t*m:
        k = 1
        while k > 0:
            tmp = k%n
            if tmp >= 10:
                tmp = str(hex(tmp))[2:]
                tmp = tmp.upper()
            result = str(tmp)+result
            k = k // n
        k += 1

    result = result[p-1::m]
    return result

print(solution(2,4,2,1))