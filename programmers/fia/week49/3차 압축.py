from collections import defaultdict


def solution(msg):
    answer = []
    dictionary = {chr(index + 64): index for index in range(1, 27)}
    linked = defaultdict(dict)
    max_index = 26
    i = 0

    while i < len(msg):
        word = msg[i]
        current = linked[word]
        i += 1

        if i >= len(msg):
            answer.append(dictionary[word])
            break

        while i < len(msg) and msg[i] in current:
            word += msg[i]
            current = current[msg[i]]
            i += 1

        answer.append(dictionary[word])

        if i < len(msg):
            max_index += 1
            dictionary[word + msg[i]] = max_index
            current[msg[i]] = {}

    return answer
