def solution(s):

    dic = {}

    s = s.replace("{", "")
    s = s.replace("}", "")
    numbers = list(map(int, s.split(",")))

    for number in numbers:
        if number in dic:
            dic[number] += 1
        else:
            dic[number] = 1

    dic_sort = sorted(dic, key=lambda x : dic[x])

    return dic_sort[::-1]