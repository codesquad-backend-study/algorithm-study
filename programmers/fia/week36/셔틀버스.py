from collections import deque


def solution(n, t, m, timetable):
    timetable.sort()
    arrivals = deque()
    bus = 9 * 60

    for time in timetable:
        hour, minu = map(int, time.split(":"))
        arrivals.append(hour * 60 + minu)

    results = [[] for _ in range(n)]

    for i in range(n):
        while arrivals and arrivals[0] <= bus and len(results[i]) < m:
            results[i].append(arrivals.popleft())

        bus += t

    answer = 0

    last = results.pop()

    if len(last) < m:
        answer = bus - t
    else:
        answer = last.pop() - 1

    answer_hour = str(answer // 60)
    answer_minu = str(answer % 60)

    return answer_hour.zfill(2) + ":" + answer_minu.zfill(2)
