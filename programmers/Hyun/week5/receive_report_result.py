def solution(id_list, report, k):
    report_log = {}
    report_cnt = {}

    for id in id_list:
        report_log[id] = set([])
        report_cnt[id] = 0

    for rep in report:
        reporter = rep.split()[0]
        report_log[reporter].add(rep.split()[1])

    for id in id_list:
        for reported_user in report_log[id]:
            report_cnt[reported_user] += 1

    ans = []

    for id, bad_users in report_log.items():
        mail = 0
        for bad_user in bad_users:
            if report_cnt[bad_user] >= k:
                mail += 1
        ans.append(mail)

    return ans