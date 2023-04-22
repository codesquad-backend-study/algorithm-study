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
        tmp2 = sign[:]
        for s in sequence :
            if s == '*' :
                tmp, tmp2 = multi(tmp,tmp2)
            elif s == '+' :
                tmp, tmp2 = sum(tmp, tmp2)
            else :
                tmp, tmp2 = sub(tmp, tmp2)
        answer.append(tmp[0])
    answer = [ abs(i) for i in answer ]
    return max(answer)

def multi(nums, sign) :
    remove = []
    for i, s in enumerate(sign) :
        if s == '*' :
            nums[i] = nums[i]*nums[i+1]
            nums[i+1] = nums[i]
            remove.append(i)
    for i in remove[-1::-1] :
        del nums[i]
        del sign[i]

    return nums, sign

def sum(nums, sign) :
    remove = []
    for i, s in enumerate(sign) :
        if s == '+' :
            nums[i] = nums[i]+nums[i+1]
            nums[i+1] = nums[i]
            remove.append(i)
    for i in remove[-1::-1] :
        del nums[i]
        del sign[i]

    return nums, sign

def sub(nums, sign) :
    remove = []
    for i, s in enumerate(sign) :
        if s == '-' :
            nums[i] = nums[i]-nums[i+1]
            nums[i+1] = nums[i]
            remove.append(i)
    for i in remove[-1::-1] :
        del nums[i]
        del sign[i]

    return nums, sign

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))