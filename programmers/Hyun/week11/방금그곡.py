def solution(m, musicinfos):
    half_steps = ["C#", "D#", "F#", "G#", "A#"]
    half_step_change = ["1", "2", "3", "4", "5"]

    matched = {}

    for idx, half in enumerate(half_steps):
        m = m.replace(half, half_step_change[idx])

    for info in musicinfos:
        start_time, end_time, title, score = info.split(",")

        for idx, half in enumerate(half_steps):
            score = score.replace(half, half_step_change[idx])

        play_time = int(end_time.split(":")[0]) * 60 + int(end_time.split(":")[1]) - (
                    int(start_time.split(":")[0]) * 60 + int(start_time.split(":")[1]))

        full_score = make_full_score(play_time, score)

        if m in full_score:
            matched[title] = play_time

    if not matched:
        return "(None)"

    return sorted(matched.items(), key=lambda x: x[1], reverse=True)[0][0]


def make_full_score(play_time, score):
    quo = play_time // len(score)
    rem = play_time % len(score)

    return score * quo + score[:rem]

