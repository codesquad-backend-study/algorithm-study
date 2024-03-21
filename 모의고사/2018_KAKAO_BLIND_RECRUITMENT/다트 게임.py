# 3번의 기회
# 기회마다 0점 ~ 10점
# S, D-2제곱, T-3제곱
# * -> 지금까지의 점수 2배, # -> 해당 점수 빼기
# 총점은?

def solution(dartResult):
    shots = []
    scores = [0, 0, 0]
    bonus_map = {'S': 1, 'D': 2, 'T': 3}

    s = 0
    for i in range(len(dartResult)):
        if dartResult[i].isalpha():
            if i < len(dartResult) - 1 and dartResult[i + 1] in ['*', '#']:
                shots.append(dartResult[s:i + 2])
                s = i + 2
            else:
                shots.append(dartResult[s:i + 1])
                s = i + 1

    for idx, shot in enumerate(shots):
        if shot[1] == '0':
            score = int(shot[0:2])
            bonus = shot[2]
        else:
            score = int(shot[0])
            bonus = shot[1]

        scores[idx] = score ** bonus_map[bonus]

        if shot[-1] in ['*', '#']:
            if shot[-1] == '*':
                if idx >= 1:
                    scores[idx - 1] *= 2
                scores[idx] *= 2
            else:
                scores[idx] *= -1

    return sum(scores)
