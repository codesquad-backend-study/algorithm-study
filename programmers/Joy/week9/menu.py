def solution(orders, course):

    dic = {}

    for order in orders :
        for alpha in order :
            if alpha in dic :
                dic[alpha] += 1
            else :
                dic[alpha] = 1

    lst = sorted(dic, key=lambda x:-dic[x])
    answer = []
    max = 0

    for c in course : # 2,3,4
        tmp = lst[:c] # AC
        tmp_times = 0
        for order in orders :
            for idx in c :
                if tmp[idx] not in order :
                    break
                tmp_times += 1
        if tmp_times >= max :
            max = tmp_times
        if max >= dic[lst[c]] :
            answer.append(tmp)


    answer = answer.sort()

solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])