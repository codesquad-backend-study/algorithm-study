def solution(n, k):
    answer = 0
    
    convert = ""
    
    while(n != 0):
        convert += str(n%k)
        n = n // k
    convert = convert[::-1]
        
    convert = convert.split("0")
    for num in convert:
        if num != "" and isPrime(int(num)):
            answer += 1
    
    return answer

def isPrime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(solution(437674, 3))
# print(solution(110011, 10))