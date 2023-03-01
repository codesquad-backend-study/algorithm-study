def solution(id_list, report, k):

    times = {id : 0 for id in id_list} #신고받은 횟수
    people = {id : [] for id in id_list} #신고받은 사람 : 신고한 사람
    mail = {id : 0 for id in id_list} #메일받을 횟수(결과)


    report = list(set(report))

    for r in report:
        reporter, reported = r.split(' ')
        times[reported] += 1
        people[reported].append(reporter)

    stopped = [id for id, v in times.items() if v >= k ] #정지된 아이디

    for i in stopped:
        list2 = people[i]
        for j in list2:
            mail[j] += 1

    answer = list(mail.values())
    return answer