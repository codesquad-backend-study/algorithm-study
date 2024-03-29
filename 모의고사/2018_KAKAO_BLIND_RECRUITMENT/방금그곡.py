# 시작 시간, 끝난 시간, 제목, 악보
# 음은 1분에 1개씩 재생
# 만약 노래 재생시간보다 실제 방송시간이 길면, 반복재생

# m 은 네오가 기억한 멜로디
# musicinfos 는 곡의 정보
# 일치하는거 찾아서 노래 제목 반환 -> 없으면 "(None)" 반환

# 여러개가 부합되면, 재생 시간 제일 긴걸로, 같으면 순서대로.
def duration_convert(s, e):
    sh, sm = s.split(':')
    sd = int(sh) * 60 + int(sm)

    eh, em = e.split(':')
    ed = int(eh) * 60 + int(em)
    return ed - sd


def melody_convert(melody, m):
    new_melody = []
    for i in range(len(m)):
        if m[i] == '#':
            nm = melody[new_melody.pop() + "#"]
            new_melody.append(nm)
        else:
            new_melody.append(m[i])
    return "".join(new_melody)


def solution(m, musicinfos):
    melody = {"C#": "1", "D#": "2", "F#": "3", "G#": "4", "A#": "5", "B#": "6", "E#": "7"}
    ans = []
    neo_melody = melody_convert(melody, m)

    for idx, music in enumerate(musicinfos):
        s, e, title, melo = music.split(",")
        duration = duration_convert(s, e)

        melo = melody_convert(melody, melo)
        melo = melo * (duration // len(melo) + 1)
        melo = melo[:duration]

        if neo_melody in melo:
            ans.append((-duration, idx, title))

    if not ans:
        return "(None)"

    ans.sort()
    return ans[0][-1]
