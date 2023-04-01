def enter(nickname):
    return nickname + '님이 들어왔습니다.'


def out(nickname):
    return nickname + '님이 나갔습니다.'


def solution(record):
    tmp_answer = {}
    answer = []
    db = {}
    nickname = ''

    for r in record:
        if r.split()[0] == 'Leave':
            command, user_id = r.split()
        else:
            command, user_id, nickname = r.split()

        if command == 'Enter':
            tmp_answer[nickname] = answer.append(enter(nickname))
            db[user_id] = nickname
        elif command == 'Leave':
            tmp_answer[nickname] = answer.append(out(db[user_id]))
            del db[user_id]
        elif command == 'Change':
            tmp_answer[db[user_id]] = answer.append(enter(nickname))
            db[user_id] = nickname

    print(tmp_answer)

    return answer


print(solution(
    ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
