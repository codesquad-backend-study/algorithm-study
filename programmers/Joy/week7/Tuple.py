def solution(s):

    lst = s.split("}")
    lst2 = [ s.replace(",","") for s in lst]
    lst2 = [ s.replace("{","") for s in lst2]
    lst2 = [ s for s in lst2 if s!='']

    lst2.sort()

    s1 = ''
    answer = []
    for i in lst2 : #['2', '21', '213', '2134']
        for s in i:
            if s not in s1:
                answer.append(s)
                s1 = i
                break
    return answer

a = solution("{{123}}")
print(a)