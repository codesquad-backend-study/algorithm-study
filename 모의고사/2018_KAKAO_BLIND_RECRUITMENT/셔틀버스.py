import collections


def solution(n, t, m, timetable):
    wait_queue = []
    for time in timetable:
        wait_queue.append(int(time[0:2]) * 60 + int(time[3:]))

    wait_queue.sort()
    wait_queue = collections.deque(wait_queue)

    shuttle_time = 540
    last_arrival_time = 540
    cnt = 0
    while n > 0:
        cnt = 0
        n -= 1
        for _ in range(m):
            if wait_queue and wait_queue[0] <= shuttle_time:
                last_arrival_time = wait_queue.popleft()
                cnt += 1
        shuttle_time += t

    shuttle_time -= t
    need_time = -1
    if cnt == m:
        need_time = last_arrival_time - 1
    else:
        need_time = shuttle_time

    hour = need_time // 60
    minute = need_time % 60

    ans = ""
    if hour < 10:
        ans += "0" + str(hour)
    else:
        ans += str(hour)

    ans += ":"

    if minute < 10:
        ans += "0" + str(minute)
    else:
        ans += str(minute)

    return ans
