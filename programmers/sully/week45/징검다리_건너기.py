from typing import List


def solution(stones: List[int], k: int) -> int:
    answer = 1
    lt, rt = 1, max(stones)

    while lt <= rt:
        mid = (lt + rt) // 2
        movable = True
        blank = 0

        for stone in stones:
            if stone < mid:
                blank += 1
                # k개의 공백이 생겼을 때, 더는 움직일 수 없게끔 false로
                if blank == k:
                    movable = False

                continue

            blank = 0

        if movable:
            answer = max(answer, mid)
            lt = mid + 1
            continue

        rt = mid - 1

    return answer
