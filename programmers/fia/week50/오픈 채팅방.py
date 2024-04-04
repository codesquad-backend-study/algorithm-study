def solution(record):
    users = {}
    messages = []
    message_types = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}

    for log in record:
        log = log.split()
        command = log[0]
        uid = log[1]

        if command == "Enter":
            users[uid] = log[2]
            messages.append((uid, command))
        elif command == "Leave":
            messages.append((uid, command))
        else:  # Change
            users[uid] = log[2]

    answer = []
    for uid, message_type in messages:
        answer.append(users[uid] + message_types[message_type])

    return answer
