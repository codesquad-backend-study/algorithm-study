from typing import List


def solution(m: str, musicinfos: List[str]) -> str:
    answer = '(None)'
    m = m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a').replace('B#', 'b').replace('E#', 'e')
    title_time = {}

    for mus in musicinfos:
        start, end, title, music = mus.split(',')
        music = music.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a').replace('B#', 'b').replace('E#', 'e')
        time = (int(end.split(':')[0]) * 60 + int(end.split(':')[1])) - (
                int(start.split(':')[0]) * 60 + int(start.split(':')[1]))

        tmp_music = ''
        is_time, i = 0, 0
        while is_time != time:
            if i == len(music):
                i = 0

            tmp_music += music[i]
            is_time += 1
            i += 1

        max_time = 0
        for i in range(len(tmp_music)):
            if tmp_music[i:len(m) + i] == m:
                if max_time < time:
                    max_time = time
                    title_time[title] = time

                answer = max(title_time, key=title_time.get)

    return answer


print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
