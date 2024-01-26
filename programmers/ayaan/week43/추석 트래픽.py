def solution(lines):
    answer = 0
    times = []
    for line in lines:
        hour = int(line[11:13])
        minute = int(line[14:16])
        second = float(line[17:23])
        t = float(line[24:-1])

        end_time = hour * 3600 + minute * 60 + second
        # 시작시간_초 = 초 - 처리량 + 0.001
        start_sec = round(second - t, 3) + 0.001
        if start_sec < 0:
            minute -= 1
            start_sec += 60
            if minute < 0:
                hour -= 1
                minute += 60
        start_time = hour * 3600 + minute * 60 + start_sec
        times.append([start_time, end_time])

    for i in range(len(times)):
        # 시작시간 ~ +1초 사이의 처리량
        init_time = times[i][0]
        plus_one = init_time + 1
        count = 0

        for time in times:
            if init_time <= time[0] < plus_one or init_time <= time[1] < plus_one:
                count += 1
            elif time[0] < init_time and plus_one < time[1]:
                count += 1
        answer = max(answer, count)

        # 종료시간 ~ +1초 사이의 처리량
        init_time = times[i][1]
        plus_one = init_time + 1
        count = 0

        for time in times:
            if init_time <= time[0] < plus_one or init_time <= time[1] < plus_one:
                count += 1
            elif time[0] < init_time and plus_one < time[1]:
                count += 1
        answer = max(answer, count)

    return answer



solution(["2016-09-15 01:00:04.002 2.0s"])
