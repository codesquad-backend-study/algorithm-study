import re

def solution(s):
    answer = []
    string = s[1:-1]
    print(string)
    temp = list(re.split(r'[{}]', string))
    temp.remove('')
    temp.remove('')
    for i in range(len(temp) // 2):
        temp.remove( ',')
    for element in temp:
        element = element[1:-1]
    temp.sort(key=len)
    print(temp)
    for asdf in temp:
        for index in range(len(asdf) // 2):
            if not answer in asdf[index*2]:
                answer.append(asdf[index*2])
                
    return answer
