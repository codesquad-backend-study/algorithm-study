def solution(id_list, report, k):
    answer = []
    
    list = {}
    mail_id = {}
    for id in id_list:
        list[id] = []
        mail_id[id] = 0
    
    for s in report:
        data = s.split()
        a = data[0]
        b = data[1]
        
        list[b].append(a)
    
    for id in id_list:
        report_list = list[id]
        count = len(set(report_list))
        if count >= k:
            for report_id in report_list:
                mail_id[report_id] += 1
    
    for key in mail_id:
        answer.append(mail_id[key])
    
    return answer

#result = solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","muzi frodo","muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 1)
result = solution(["a", "b"], ["b a"], 1)
print(result)