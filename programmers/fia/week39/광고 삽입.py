def solution(play_time, adv_time, logs):
    # 동영상 시간 변환
    h, m, s = map(int, play_time.split(":"))
    play_time_number = h * 3600 + m * 60 + s

    # 광고 시간 변환
    h, m, s = map(int, adv_time.split(":"))
    adv_time_number = h * 3600 + m * 60 + s

    if play_time_number == adv_time_number:
        return "00:00:00"

    times = [0] * (play_time_number + 1)

    for log in logs:
        start, end = log.split("-")

        # 시작 시간 변환
        h, m, s = map(int, start.split(":"))
        start_number = h * 3600 + m * 60 + s

        # 끝 시간 변환
        h, m, s = map(int, end.split(":"))
        end_number = h * 3600 + m * 60 + s

        times[start_number] += 1
        times[end_number] -= 1

    for i in range(1, len(times)):
        times[i] += times[i - 1]

    for i in range(1, len(times)):
        times[i] += times[i - 1]

    max_times = times[adv_time_number - 1]
    max_start = 0

    for i in range(adv_time_number, play_time_number + 1):
        total = times[i] - times[i - adv_time_number]

        if total > max_times:
            max_times = total
            max_start = i - adv_time_number + 1

    h = str(max_start // 3600).zfill(2)
    m = str((max_start % 3600) // 60).zfill(2)
    s = str(((max_start % 3600) % 60)).zfill(2)

    return h + ":" + m + ":" + s
