import re


def solution(dartResult):
    results = re.findall(r'\d+[S,D,T,*,#]+', dartResult)
    total = []

    for result in results:
        result = result.replace('10', '!', 3)
        point = 10 if result[0] == '!' else int(result[0])

        if result[1] == 'D':
            point = point ** 2
        elif result[1] == 'T':
            point = point ** 3

        if len(result) == 3:
            if result[2] == '*':
                if total:
                    total[-1] = total[-1] * 2
                point = point * 2
            else:
                point *= -1

        total.append(point)

    return sum(total)
