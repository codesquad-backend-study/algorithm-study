def solution(numbers, hand):
    def find_distance(target, current):
        tx, ty = points[target]
        cx, cy = points[current]

        return abs(tx - cx) + abs(ty - cy)

    points = {1: (0, 0), 2: (1, 0), 3: (2, 0),
              4: (0, 1), 5: (1, 1), 6: (2, 1),
              7: (0, 2), 8: (1, 2), 9: (2, 2),
              '*': (0, 3), 0: (1, 3), '#': (2, 3)}

    default = {1: 'L', 3: 'R', 4: 'L', 6: 'R',
               7: 'L', 9: 'R'}

    hand = 'L' if hand == 'left' else 'R'
    left = '*'
    right = '#'
    answer = ''

    for number in numbers:
        if number in default:
            answer += default[number]
            if default[number] == 'L':
                left = number
            else:
                right = number
        else:
            left_distance = find_distance(number, left)
            right_distance = find_distance(number, right)

            if left_distance < right_distance:
                left = number
                answer += 'L'
            elif left_distance > right_distance:
                right = number
                answer += 'R'
            else:
                if hand == 'L':
                    left = number
                else:
                    right = number
                answer += hand

    return answer
