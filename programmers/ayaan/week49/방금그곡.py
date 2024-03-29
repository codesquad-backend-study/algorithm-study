def solution(m, musicinfos):
    temp = [('C#', 'c'), ('D#', 'd'), ('F#', 'f'), ('G#', 'g'), ('A#', 'a'), ('B#', 'b'), ('E#', 'e')]
    for a in temp:
        m = m.replace(a[0], a[1])

    musics = []
    for info in musicinfos:
        infos = info.split(',')
        start_time = int(infos[0][0:2]) * 60 + int(infos[0][3:5])
        end_time = int(infos[1][0:2]) * 60 + int(infos[1][3:5])
        time = end_time - start_time

        melody = infos[3]
        for a in temp:
            melody = melody.replace(a[0], a[1])

        music = melody * (time // len(melody))
        music += melody[:(time % len(melody))]

        if m in music:
            musics.append((time, infos[2]))

    answer = '(None)'
    max_time = 0
    for music in musics:
        if max_time < music[0]:
            answer = music[1]
            max_time = music[0]

    return answer
