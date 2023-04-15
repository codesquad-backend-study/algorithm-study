def solution(n, t, m, p):
    convertList = ['0','1']
    
    # t : 구할 숫자의 개수, m : 참가인원
    # t * m 까지 n진수로 변환
    for i in range(2, t*m):
        convertStr = nZinSu(i, n)
        for ch in convertStr:
            convertList.append(ch)
    
    result = ""
    for i in range(p-1, t*m, m):
        result += convertList[i]
        
    return result
        

def nZinSu(num, n):
    result = ""
    while(num != 0):
        a = num % n
        if a > 9:
            result += chr(a - 10 + ord('A'))
        else:
            result += str(num % n)
        num = num // n
    return result[::-1]


print(solution(16, 16, 2, 1))