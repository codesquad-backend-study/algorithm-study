def solution(record):
    
    answer = []
    id_nickname = {}
    message = {'Enter':'들어왔습니다.', 'Leave':'나갔습니다.'}

    for r in record :
        if 'Leave' not in  r :
            tmp = r.split(' ')
            id_nickname[tmp[1]] = tmp[2]
    
    for r in record :
        if 'Change' not in r :
            tmp = r.split(' ')
            nickname = id_nickname[tmp[1]]
            s = nickname+"님이 "+message[tmp[0]]
            answer.append(s)
    
    return answer