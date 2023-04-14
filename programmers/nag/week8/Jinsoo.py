def solution(n, t, m, p):
    answer = ''
    if n <= 10:
        dic = {i: i for i in range(n)}
    else:
        dic = {i: i for i in range(10)}
        dic.update({i: chr(ord('A') + i - 10) for i in range(10, n)})
    
    mod = ''
    number = 0
    while len(answer) < t:
        while len(mod) < m:
            temp = number
            while temp > 0:
                mod = mod + str(dic[temp // n])
                temp = temp % n
            print(mod)
            number += 1
        answer = answer + mod[p-1]
        mod = mod[m:]
    return answer
