# [닉네임]님이 들어왔습니다.
# [닉네임]님이 나갔습니다.

# 채팅방을 나간 후 닉네임을 변경하거나, 채팅방 안에서 닉네임을 변경한다.
# 닉네임 변경 시 기존 메시지의 닉네임도 전부 변경된다.
# 중복 닉네임을 허용한다.

# 채팅방 입퇴장, 닉네임 변경 기록이 담긴 record 배열
## Enter uuid 닉네임
## Leave uuid 닉네임
## Change uuid 닉네임
## 단어는 알파벳 대소문자, 숫자로만 이루어짐

# 방에 쌓인 최종적인 메시지를 문자열 형태로 반환
def solution(record):
    logs = []
    session = {}
    for each in record:
        splited = each.split()  # command, uuid, (nickname)
        command, uuid = splited[0], splited[1]
        if command == 'Leave':
            logs.append((uuid, 'L'))
        else:
            nickname = splited[2]
            session[uuid] = nickname
            if command == 'Enter':
                logs.append((uuid, 'E'))

    ans = []
    for uuid, typ in logs:
        if typ == 'E':
            ans.append(session[uuid] + '님이 들어왔습니다.')
        else:
            ans.append(session[uuid] + '님이 나갔습니다.')

    return ans
