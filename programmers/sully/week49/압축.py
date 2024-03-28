from typing import List


def solution(msg: str) -> List[int]:
    answer: List[int] = []

    msg = msg.upper()
    words = {chr(ord('A') + i): i + 1 for i in range(26)}

    idx = 0
    while idx < len(msg):
        word = ''
        contains = False

        while idx < len(msg):
            word += msg[idx]

            if word not in words:
                contains = True
                break

            idx += 1

        if contains:
            words[word] = len(words) + 1
            answer.append(words[word[:-1]])
        else:
            answer.append(words[word])
            break

    return answer


print(solution('KAKAO'))
