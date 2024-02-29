def solution(s):
    answer = ''
    numbers = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
               'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    number = ''
    for c in s:
        if c.isdigit():
            answer += c
        else:
            number += c
            if number in numbers:
                answer += numbers[number]
                number = ''

    return int(answer)

solution("one4seveneight")
