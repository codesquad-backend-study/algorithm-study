def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        b1 = bin(arr1[i])[2:]
        if len(b1) < n:
            zero = '0' * (n - len(b1))
            b1 = zero + b1
        b2 = bin(arr2[i])[2:]
        if len(b2) < n:
            zero = '0' * (n - len(b2))
            b2 = zero + b2

        l = ''
        for i in range(n):
            if b1[i] == '0' and b2[i] == '0':
                l += ' '
            else:
                l += '#'
        answer.append(l)

    return answer
