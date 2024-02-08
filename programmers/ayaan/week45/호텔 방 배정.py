import collections


def solution(k, room_number):
    answer = []
    visited = collections.defaultdict(int)
    for num in room_number:
        temp = [num]
        if visited[num] == 0:
            visited[num] = num + 1
            answer.append(num)
        else:
            next = visited[num]
            while True:
                if visited[next] == 0:
                    visited[next] = next + 1
                    answer.append(next)

                    # 이전에 거쳐온 방들도 현재 번호로 갱신해준다
                    for prev in temp:
                        visited[prev] = next + 1
                    break
                else:
                    next = visited[next]
                    # 이전 방을 temp에 담아둔다
                    temp.append(next)

    return answer
