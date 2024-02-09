def solution(k, room_number):
    rooms = {}
    ans = []
    for want in room_number:
        if want not in rooms:
            rooms[want] = want + 1
            ans.append(want)
        else:
            visit = [want]
            next_loc = rooms[want]
            while next_loc in rooms:
                visit.append(next_loc)
                next_loc = rooms[next_loc]
            rooms[next_loc] = next_loc + 1
            ans.append(next_loc)
            for each in visit:
                rooms[each] = next_loc + 1

    return ans
