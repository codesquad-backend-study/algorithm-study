def solution(play_time, adv_time, logs):
    def convert(str_time):
        time = str_time.split(':')
        return (int(time[0]) * 60 * 60) + (int(time[1]) * 60) + int(time[2])

    play_time = convert(play_time)
    adv_time = convert(adv_time)
    total_time = [0] * (play_time + 1)

    for log in logs:
        split_log = log.split('-')
        start_time = convert(split_log[0])
        end_time = convert(split_log[1])
        # 시작시간은 + 1
        total_time[start_time] = total_time[start_time] + 1
        # 종료시간은 - 1
        total_time[end_time] = total_time[end_time] - 1

    # 누적합 : 해당 시간에 시청한 사람 숫자
    for i in range(1, play_time + 1):
        total_time[i] = total_time[i] + total_time[i - 1]
    # 한번 더 누적합 구하면 해당 시간에 모든 사람들의 재생 시간을 구할 수 있다.
    for i in range(1, play_time + 1):
        total_time[i] = total_time[i] + total_time[i - 1]

    answer = 0
    max_time = total_time[adv_time]
    for i in range(adv_time, play_time):
        if max_time < total_time[i] - total_time[i - adv_time]:
            max_time = total_time[i] - total_time[i - adv_time]
            answer = i - adv_time + 1

    hour = answer // 3600
    answer = answer - hour * 3600
    min = answer // 60
    sec = answer % 60

    return str(hour).zfill(2) + ':' + str(min).zfill(2) + ':' + str(sec).zfill(2)

solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"])
