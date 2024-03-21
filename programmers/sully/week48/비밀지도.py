from typing import List


def solution(n: int, arr1: List[int], arr2: List[int]) -> List[str]:
    answer: List[str] = []
    BLANK, WALL = ' ', '#'

    for i in range(n):
        result = (
            # OR 연산 (둘 중 하나만 포함되면 되니)
            bin(arr1[i] | arr2[i])[2:]
            # Java에서는 format 쓰는 것과 같은 원리로 n글자에 맞춰서 앞에 0을 붙여줌
            .zfill(n)
            .replace('1', WALL)
            .replace('0', BLANK)
        )

        answer.append(result)

    return answer
