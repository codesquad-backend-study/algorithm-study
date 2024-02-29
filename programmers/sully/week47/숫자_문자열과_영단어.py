def solution(s: str) -> int:
    answer = ''
    numbers_hash = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
                    'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    tmp = ''
    for c in s:
        if c.isdigit():
            answer += c
            continue

        tmp += c

        if tmp in numbers_hash:
            answer += str(numbers_hash[tmp])
            tmp = ''

    return int(answer)


print(solution("one4seveneight"))
