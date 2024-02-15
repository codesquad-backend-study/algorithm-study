def solution(numbers, hand):
    answer = ''
    keypad = {}
    for num in range(9):
        keypad[num + 1] = (num // 3, num % 3)
    keypad[0] = (3, 1)
    keypad[-1] = (3, 0)
    keypad[-2] = (3, 2)

    def distance(num1, num2):
        a = keypad[num1]
        b = keypad[num2]
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    left = -1
    right = -2

    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            left = number
        elif number in [3, 6, 9]:
            answer += 'R'
            right = number
        else:
            if distance(number, left) < distance(number, right):
                answer += 'L'
                left = number
            elif distance(number, left) > distance(number, right):
                answer += 'R'
                right = number
            else:
                if hand == 'left':
                    answer += 'L'
                    left = number
                else:
                    answer += 'R'
                    right = number

    return answer
