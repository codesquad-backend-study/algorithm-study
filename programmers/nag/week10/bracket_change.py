def solution(p):
    answer = ''
    split = []
    left = 0
    right = 0
    temp = ''
    for c in p:
        if c == '(':
            left += 1
        else:
            right += 1
        temp = temp + c
        if left == right:
            split.append(temp)
            temp = ''
    for element in reversed(split):
        if element[0] == '(':
            answer = element + answer
        else:
            temp = element[1:-1]
            answer = '(' + answer + ')' + temp[::-1]
    return answer
