# 9시부터 n 회 t 분 간격으로 버스가 온다.
# 버스는 최대 m 명 태운다.

import heapq


def solution(n, t, m, timetable):
    def str_to_time(str_time):
        hour, minute = str_time.split(":")
        return int(hour) * 60 + int(minute)

    def time_to_str(time):
        hour = time // 60
        minute = time % 60
        return str(hour).zfill(2) + ":" + str(minute).zfill(2)

    heap = []
    for time in timetable:
        heapq.heappush(heap, str_to_time(time))

    bus_time = 540
    last_passenger = -1
    passenger_count = 0

    while True:
        for _ in range(m):
            if heap and bus_time >= heap[0]:
                last_passenger = heapq.heappop(heap)
                passenger_count += 1

        n -= 1
        if n == 0:
            break
        bus_time += t
        passenger_count = 0

    if passenger_count == m:  # 만약 대기열때문에 버스를 다 못타는 경우
        return time_to_str(last_passenger - 1)
    else:
        return time_to_str(bus_time)
