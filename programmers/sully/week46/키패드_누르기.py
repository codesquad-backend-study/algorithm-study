from typing import List


def solution(numbers: List[int], hand: str) -> str:
    LEFT = 'L'
    RIGHT = 'R'
    answer = ''

    # 왼손: 1, 4, 7
    # 오른손: 3, 6, 9
    # 더 가까운 손: 2, 5, 8, 0
    left_hash = {1: (0, 3), 4: (0, 2), 7: (0, 1)}
    right_hash = {3: (2, 3), 6: (2, 2), 9: (2, 1)}
    near_hash = {2: (1, 3), 5: (1, 2), 8: (1, 1), 0: (1, 0)}

    start_left_hand, start_right_hand = (0, 0), (2, 0)
    for number in numbers:
        if number in left_hash:
            answer += LEFT
            start_left_hand = left_hash[number]
            continue

        if number in right_hash:
            answer += RIGHT
            start_right_hand = right_hash[number]
            continue

        # near_hash 시작

        # x좌표 + y좌표
        current_left_distance = abs(near_hash[number][0] - start_left_hand[0]) + abs(
            near_hash[number][1] - start_left_hand[1])
        current_right_distance = abs(near_hash[number][0] - start_right_hand[0]) + abs(
            near_hash[number][1] - start_right_hand[1])

        if current_left_distance < current_right_distance:
            answer += LEFT
            start_left_hand = near_hash[number]
            continue

        if current_left_distance > current_right_distance:
            answer += RIGHT
            start_right_hand = near_hash[number]
            continue

        # if current_left_distance == current_right_distance:
        # 왼손잡이인지, 오른손잡이인지 확인
        if hand == 'left':
            answer += LEFT
            start_left_hand = near_hash[number]
            continue
        # elif hand == 'right':
        answer += RIGHT
        start_right_hand = near_hash[number]

    return answer
