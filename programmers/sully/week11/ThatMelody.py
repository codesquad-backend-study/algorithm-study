def solution(m, musicinfos):
    answer = '(None)'
    m = m.replace('C#', 'C').replace('D#', 'D').replace('F#', 'F').replace('G#', 'G').replace('A#', 'A')

    for mus in musicinfos:
        start, end, title, music = mus.split(',')
        # 위에서 했던 것처럼 리플레이스
        music = music.replace('C#', 'C').replace('D#', 'D').replace('F#', 'F').replace('G#', 'G').replace('A#', 'A')
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
        for i in range(len(tmp_music)):
            if tmp_music[i] == m[0]:
                if tmp_music[i:len(m) + i] == m:
                    answer = title
                    break

    return answer


# HELLO
print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
