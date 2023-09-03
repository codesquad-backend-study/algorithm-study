import heapq
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        answer: List[List[int]] = []
        heap = []

        for person in people:
            # (그 사람의 키, 자신의 키 이상인 사람들의 수) -> 최대힙으로
            # 즉, 키가 큰 사람부터 처리할 수 있게 됨
            heapq.heappush(heap, (-person[0], person[1]))

        while heap:
            # 키가 가장 큰 사람을 pop
            person = heapq.heappop(heap)
            # person[1]번째 index에 _object 추가
            # 왜냐면 person[1]은 자신의 키 이상인 사람들의 수이므로 index에 삽입하는 거임
            answer.insert(person[1], [-person[0], person[1]])

        return answer
