from collections import deque


def solution(n, t, m, timetable):
    times = []

    for time in timetable:
        hour, minute = map(int, time.split(":"))
        time = hour * 60 + minute
        times.append(time)

    times.sort()
    times = deque(times)

    first = 60 * 9
    passengers = []

    for i in range(n):
        arrived_at = first + i * t
        temp = []

        while times and len(temp) < m and times[0] <= arrived_at:
            temp.append(times.popleft())

        passengers.append(temp)

    if len(passengers[-1]) < m:
        last = first + (n - 1) * t
    else:
        last = passengers[-1][-1] - 1

    return str(last // 60).zfill(2) + ":" + str(last % 60).zfill(2)
