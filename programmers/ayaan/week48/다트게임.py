def solution(dartResult):
    answer = 0

    scores = []
    i = 0
    for cnt in range(3):
        # 점수
        score = 0
        if dartResult[i + 1] == '0':
            score += 10
            i += 2
        else:
            score += int(dartResult[i])
            i += 1

        # 보너스
        if dartResult[i] == 'D':
            score = score ** 2
        elif dartResult[i] == 'T':
            score = score ** 3
        i += 1

        if i == len(dartResult):
            scores.append(score)
            break

        # 옵션
        if dartResult[i] == '*':
            if cnt != 0:
                scores[cnt - 1] *= 2
            score *= 2
            i += 1
        elif dartResult[i] == '#':
            score *= -1
            i += 1
        scores.append(score)

    return sum(scores)
