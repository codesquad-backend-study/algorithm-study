def solution(lines):
    log = []

    for line in lines:
        _, time, spend = line.split()
        hour, minute, second = map(float, time.split(':'))

        end_time = 3600 * int(hour) + 60 * int(minute) + second
        start_time = end_time - float(spend[:-1]) + 0.001
        log.append((start_time, end_time))

    answer = 0

    for i in range(len(log)):
        temp = 1

        for j in range(i + 1, len(log)):
            # 끝나는 시간을 기준으로 정렬했기 때문에 비교의 기준은 끝나는 시간이 되어야 한다
            if log[j][1] - log[i][1] > 4:  # end time - end time > 4
                break
            # 시작하는 시간이 기준이 되는 끝나는 시간 + 1 안에 위치할 때 작업의 수 + 1
            if log[j][0] < log[i][1] + 1:  # start time < end time + 1
                temp += 1

        answer = max(answer, temp)

    return answer
