def solution(k, room_number):
    answer = []
    next_room = {}

    for rn in room_number:
        if rn not in next_room:
            answer.append(rn)
            next_room[rn] = rn + 1
        else:
            current = rn
            update_need = []

            while current in next_room:
                update_need.append(current)
                current = next_room[current]

            answer.append(current)
            next_room[current] = current + 1

            for unr in update_need:
                next_room[unr] = current + 1

    return answer
