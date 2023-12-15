def solution(play_time, adv_time, logs):
    MAX = 360000
    logs_start_sec = []
    logs_end_sec = []
    play_time_sec = int(play_time.split(':')[0]) * 3600 + int(play_time.split(':')[1]) * 60 + int(
        play_time.split(':')[2])
    adv_time_sec = int(adv_time.split(':')[0]) * 3600 + int(adv_time.split(':')[1]) * 60 + int(adv_time.split(':')[2])

    for each in logs:
        start, end = each.split('-')
        h, m, s = map(int, start.split(':'))

        s += h * 3600 + m * 60
        logs_start_sec.append(s)

        h, m, s = map(int, end.split(':'))
        s += h * 3600 + m * 60
        logs_end_sec.append(s)

    total_time = [0] * MAX

    for i in range(len(logs)):
        total_time[logs_start_sec[i]] += 1
        total_time[logs_end_sec[i]] -= 1

    for i in range(1, play_time_sec):
        total_time[i] = total_time[i] + total_time[i - 1]

    for i in range(1, play_time_sec):
        total_time[i] = total_time[i] + total_time[i - 1]

    max_time = -1
    max_start_time = -1

    for i in range(adv_time_sec - 1, play_time_sec):
        if i == adv_time_sec - 1:
            if max_time < total_time[i]:
                max_time = total_time[i]
                max_start_time = 0
        else:
            if max_time < total_time[i] - total_time[i - adv_time_sec]:
                max_time = total_time[i] - total_time[i - adv_time_sec]
                max_start_time = i - adv_time_sec + 1

    h = max_start_time // 3600
    m = max_start_time % 3600 // 60
    s = max_start_time % 3600 % 60

    ans = ""
    if h < 10:
        ans += '0' + str(h) + ':'
    else:
        ans += str(h) + ':'

    if m < 10:
        ans += '0' + str(m) + ':'
    else:
        ans += str(m) + ':'

    if s < 10:
        ans += '0' + str(s)
    else:
        ans += str(s)

    return ans
