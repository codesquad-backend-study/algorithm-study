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
            print(answer)
        else:
            temp = element[1:-1]
            asdf = ''
            for c in temp:
                if c == '(':
                    asdf = asdf + ')'
                else:
                    asdf = asdf + '('
            answer = '(' + answer + ')' + asdf
    return answer
