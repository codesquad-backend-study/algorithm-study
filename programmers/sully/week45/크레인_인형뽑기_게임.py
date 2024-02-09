import collections
from typing import List


def solution(board: List[List[int]], moves: List[int]) -> int:
    answer = 0
    basket = collections.deque()
    basket.append(0)

    # 이 크레인 move 한 번마다 board 전체 순회를 하니
    for move in moves:
        for y in range(len(board)):
            # move가 1부터 시작하니
            current = board[y][move - 1]

            # 이미 뽑은 인형이면
            if current == 0:
                continue

            # 바구니에 2개 연속으로 쌓이면
            if basket[-1] == current:
                basket.pop()
                answer += 2
            else:
                basket.append(current)

            # 현재 뽑은 인형 0으로 표시 후 다음 move로 넘어가기
            board[y][move - 1] = 0
            break

    return answer
