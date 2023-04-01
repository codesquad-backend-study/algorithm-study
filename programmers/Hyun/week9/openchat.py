def solution(record):
    session = {}

    for each in record:
        splited = each.split()

        ins = splited[0]
        uuid = splited[1]

        if ins != "Leave":
            nickname = splited[2]
            session[uuid] = nickname

    ans = []
    for each in record:
        s = ""

        splited = each.split()

        ins = splited[0]
        uuid = splited[1]

        if ins == "Enter":
            s += session[uuid] + "님이 들어왔습니다."
        elif ins == "Leave":
            s += session[uuid] + "님이 나갔습니다."
        else:
            continue

        ans.append(s)

    return ans
