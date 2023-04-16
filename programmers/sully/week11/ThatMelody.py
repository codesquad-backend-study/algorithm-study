def solution(m, musicinfos):
    answer = '(None)'
    m = m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')

    for mus in musicinfos:
        start, end, title, music = mus.split(',')
        # 위에서 했던 것처럼 리플레이스
        music = music.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
        # start, end 미닛으로 변환 + 음은 1분에 1개씩 재생됨 (즉, time이 재생되는 횟수이기도 함)
        time = (int(end.split(':')[0]) * 60 + int(end.split(':')[1])) - (
                int(start.split(':')[0]) * 60 + int(start.split(':')[1]))

        # music을 계속해서 time번 tmp_music에 더해주기
        tmp_music = ''
        is_time, i = 0, 0
        while is_time != time:
            # i가 music의 길이보다 더 길면 0으로 다시 초기화해줘서 계속계속 돌아주는 로직
            if i == len(music):
                i = 0

            tmp_music += music[i]

            is_time += 1
            i += 1

        # tmp_music 전체가 m에 포함이 되면 (find, in 쓰면 안 됨)
        # 더 긴 거?
        title_time = {}
        maxTime = 0
        for i in range(len(tmp_music)):
            if tmp_music[i:len(m) + i] == m:
                # 조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다.
                # 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.
                # 현재 시간이 더 길 경우
                if maxTime < time:
                    answer = title
                    maxTime = time
                    title_time[title] = time
                # 재생된 시간이 더 작거나 같을 경우
                else:


                # title_time[title] = time
                # answer = title
    return answer


# HELLO
print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
