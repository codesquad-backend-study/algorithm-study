import re
import math

def solution(n, k):
    answer = -1
    mod = ''
    while n > 0:
        mod = str(n % k) + mod
        n = n // k
    number = list(map(int, re.split(r'[0]{1,}', mod)))
    print(number)
    cnt = 0
    for n in number:
        prime = False
        
        if n == 1:
            continue
        if n == 2 or 3:
            prime = True
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                prime = False
                break
            prime = True
        if prime:
            cnt += 1
    return cnt
