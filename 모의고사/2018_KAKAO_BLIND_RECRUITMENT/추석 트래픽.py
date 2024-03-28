# 처리시간은 시작시간과 끝시간을 포함
# 완료시간 - 처리시간 - 0.001 = 시작시간
# lines 는 응답 완료 시간을 기준으로 오름차순 정렬

# 초당 최대 처리량을 반환

def solution(lines):
    # 시작 시간 다 구하고, 정렬하고, 시작 지점을 기준으로 1초동안 개수세기

    # 시간 구하기
    times = []
    for line in lines:
        _, end_time, duration = line.split()
        h, m, s, mm = int(end_time[0:2]), int(end_time[3:5]), int(end_time[6:8]), int(end_time[9:])
        d = float(duration[:-1]) * 1000

        end_time = h * 60 * 60 * 1000 + m * 60 * 1000 + s * 1000 + mm
        start_time = end_time - d + 1

        times.append((end_time, start_time))

    # 정렬하기
    times.sort()

    # 개수세기
    max_tps = 1
    for i in range(len(times) - 1):
        fivot_end_time, _ = times[i]
        tps = 1
        for j in range(i + 1, len(times)):
            _, start_time = times[j]
            if start_time < fivot_end_time + 1000:
                tps += 1
        max_tps = max(max_tps, tps)

    return max_tps
