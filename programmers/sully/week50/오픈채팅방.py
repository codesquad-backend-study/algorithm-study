from typing import List


def solution(record: List[str]) -> List[str]:
    answer = []
    id_nickname_hash = {}
    enter_leave = []

    for r in record:
        # 명령어, 아이디, 닉네임 순서
        rr = r.split()

        if rr[0] == 'Enter':
            # id_nickname_hash[아이디] = 닉네임
            id_nickname_hash[rr[1]] = rr[2]
            enter_leave.append((rr[1], 'Enter'))
        elif rr[0] == 'Leave':
            enter_leave.append((rr[1], 'Leave'))
        elif rr[0] == 'Change':
            # id_nickname_hash[아이디] = 닉네임
            id_nickname_hash[rr[1]] = rr[2]

    for e_l in enter_leave:
        if e_l[1] == 'Enter':
            answer.append(id_nickname_hash[e_l[0]] + '님이 들어왔습니다.')
        elif e_l[1] == 'Leave':
            answer.append(id_nickname_hash[e_l[0]] + '님이 나갔습니다.')

    return answer


print(solution(
    ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
