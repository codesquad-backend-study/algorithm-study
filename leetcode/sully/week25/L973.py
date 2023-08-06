from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        answer: List[List[int]] = []

        for x, y in points:
            # 어차피 거리 비교니까 루트는 신경쓰지 않아도 될 듯
            distance = (0 - x) ** 2 + (0 - y) ** 2
            answer.append([distance, x, y])

        answer.sort(key=lambda z: z[0])

        answer = answer[:k]

        for one in answer:
            one.pop(0)

        return answer
