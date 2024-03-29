from typing import List


def to_second(time: str) -> int:
    second = 0

    time_split = time.split(':')
    h, m, s = time_split[0], time_split[1], time_split[2]

    if h < '10':
        second += int(h[1]) * 60 * 60
    else:
        second += int(h) * 60 * 60

    if m < '10':
        second += int(m[1]) * 60
    else:
        second += int(m) * 60

    if s < '10':
        second += int(s[1])
    else:
        second += int(s)

    return second


def to_time(second: int) -> str:
    h = second // 3600
    m = (second % 3600) // 60
    s = second % 60

    return to_time_str(h) + ':' + to_time_str(m) + ':' + to_time_str(s)


def to_time_str(num: int) -> str:
    if num < 10:
        return '0' + str(num)

    return str(num)


def solution(play_time: str, adv_time: str, logs: List[str]) -> str:
    answer = 0

    play_time_second = to_second(play_time)
    adv_time_second = to_second(adv_time)

    # 초당 시청자 수 (누적합 배열)
    total_viewer_for_second = [0 for _ in range(play_time_second + 1)]

    # 각 구간의 시청자 수 체크
    # total_viewer_for_second[time] = (time 시각에 시작한 시청자 수) - (time 시각에 종료한 시청자 수)
    for log in logs:
        start, end = log.split('-')
        start_sec = to_second(start)
        end_sec = to_second(end)

        total_viewer_for_second[start_sec] += 1
        total_viewer_for_second[end_sec] -= 1

    # 누적합 계산 1회 (1초 간격으로 누적합 계산)
    # total_viewer_for_second[time] = (time 시각부터 time + 1 시각까지의 1초간의 구간을 포함한 시청자 수)
    for i in range(1, len(total_viewer_for_second)):
        total_viewer_for_second[i] += total_viewer_for_second[i - 1]

    # 누적합 계산 2회 (해당 초까지의 누적 시청자 계산)
    # total_viewer_for_second[time] = (0초부터 time + 1 시각까지의 구간을 포함한 누적 시청자 수)
    for i in range(1, len(total_viewer_for_second)):
        total_viewer_for_second[i] += total_viewer_for_second[i - 1]

    max_viewer_from_zero_time = total_viewer_for_second[adv_time_second - 1]
    for i in range(0, len(total_viewer_for_second) - adv_time_second):
        target = total_viewer_for_second[i + adv_time_second] - total_viewer_for_second[i]
        if target > max_viewer_from_zero_time:
            max_viewer_from_zero_time = target
            answer = i + 1

    print(answer)
    return to_time(answer)


print(solution("02:03:55", "00:14:15",
               ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29",
                "01:37:44-02:02:30"]))
