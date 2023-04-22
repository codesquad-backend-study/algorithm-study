import re

def solution(expression):
    tmp = expression[:]
    tmp = re.sub('[^0-9]', '.', tmp)
    tmp = tmp.split('.')
    nums = [ int(s) for s in tmp ]

    tmp = expression[:]
    tmp = re.sub('[0-9]', '', tmp)
    sign = list(tmp)

    answer = []
    combin = ['*-+', '*+-', '+-*', '+*-', '-+*', '-*+']

    for sequence in combin:
        tmp = nums[:]
        for s in sequence :
            if s == '*' :
                tmp = multi(tmp,sign)
            elif s == '+' :
                tmp = sum(nums, sign)
            else :
                tmp = sub(nums, sign)
        answer.append(tmp[0])
    return max(answer)

def multi(nums, sign) :
    for i, s in enumerate(sign) :
        if s == '*' :
            nums[i] = nums[i]*nums[i+1]
            del nums[i+1]
    return nums

def sum(nums, sign) :
    for i, s in enumerate(sign) :
        if s == '+' :
            nums[i] = nums[i]+nums[i+1]
            del nums[i+1]
    return nums

def sub(nums, sign) :
    for i, s in enumerate(sign) :
        if s == '-' :
            nums[i] = nums[i]-nums[i+1]
            del nums[i+1]
    return nums

print(solution("100-200*300-500+20"	))