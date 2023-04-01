def solution(record):
    answer = []
    db = {}
    enter_leave = []

    for r in record:
        # command, user_id, nickname 순서
        rr = r.split()

        if rr[0] == 'Enter':
            # user_id = nickname
            db[rr[1]] = rr[2]
            # user_id, "Enter" 표시
            enter_leave.append((rr[1], 'Enter'))
        elif rr[0] == 'Leave':
            # user_id, "Leave" 표시
            enter_leave.append((rr[1], 'Leave'))
        elif rr[0] == 'Change':
            # user_id = nickname
            db[rr[1]] = rr[2]

    for e_l in enter_leave:
        if e_l[1] == 'Enter':
            answer.append(db[e_l[0]] + '님이 들어왔습니다.')
        elif e_l[1] == 'Leave':
            answer.append(db[e_l[0]] + '님이 나갔습니다.')

    return answer


print(solution(
    ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))

