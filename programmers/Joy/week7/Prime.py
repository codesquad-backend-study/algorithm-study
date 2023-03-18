import math

def solution(n, k):
    # 1. n -> k진법 수로 변환
    if k==10 :
        n = str(n)
    elif k == 2:
        n = bin(n)[2:]
    elif k == 8:
        n = oct(n)[2:]
    elif k == 16:
        n = hex(n)[2:]
    else :
        print("3진법")
        n = str(n)

    # 2. 수 나누기
    nums = n.split('0')
    nums = [ int(s) for s in nums if s!= '1' and s != '']

    count = 0
    for num in nums:
        for div in range(2,math.sqrt(num)+1):
            if num % div == 0:
                break
        count += 1
    return count

print(solution(110011,10))