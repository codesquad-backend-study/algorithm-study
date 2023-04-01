def solution(record):
    position = {}
    result = []
    
    for i, s in enumerate(record):
        data = s.split()
        
        if data[0] == "Enter":
            position[data[1]] = [i]
            result.append(data[2] + "님이 들어왔습니다.")
        elif data[0] == "Leave":
            position[data[1]].append(i)
            result.append(data[2] + "님이 나갔습니다.")
        else:
            history = position[data[1]]
            for idx in history:
                a = result[idx]
                nim = a.find("님")
                result[idx] = data[2] + a[nim:]
    print(result)
    
solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])