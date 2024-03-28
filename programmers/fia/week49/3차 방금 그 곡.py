def solution(m, musicinfos):
    mappings = {
        "C#": "c",
        "D#": "d",
        "F#": "f",
        "G#": "g",
        "A#": "a",
        "B#": "b"
    }
    for key, value in mappings.items():
        m = m.replace(key, value)

    max_playtime = 0
    answer = ''

    for info in musicinfos:
        start, end, title, melody = info.split(",")
        start = int(start.split(":")[0]) * 60 + int(start.split(":")[1])
        end = int(end.split(":")[0]) * 60 + int(end.split(":")[1])
        playtime = end - start

        for key, value in mappings.items():
            melody = melody.replace(key, value)

        if playtime > len(melody):
            index = 0
            while len(melody) < playtime:
                melody += melody[index]
                index += 1

        elif playtime < len(melody):
            index = len(melody) - 1
            while index + 1 > playtime:
                index -= 1
            melody = melody[:index + 1]

        if m in melody:
            if max_playtime < playtime:
                max_playtime = playtime
                answer = title

    return answer if answer else '(None)'
