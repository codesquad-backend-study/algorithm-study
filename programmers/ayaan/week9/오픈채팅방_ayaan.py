def solution(record):
    nickName = {}
    messages = []
    result = []
    
    for i, s in enumerate(record):
        data = s.split()
        
        if data[0] != "Leave":
            nickName[data[1]] = data[2]
        messages.append(data[0] + " " + data[1])
        
    for message in messages:
        command, uid = message.split()
        
        if command == "Enter":
            result.append(nickName[uid] + "님이 들어왔습니다.")
        elif command == "Leave":
            result.append(nickName[uid] + "님이 나갔습니다.")
        else:
            continue
    
    return result
    
solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])