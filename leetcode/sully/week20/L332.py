import collections
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        answer = []
        graph = collections.defaultdict(list)

        for x, y in sorted(tickets):
            graph[x].append(y)

        def dfs(x: str):
            # 재귀로 다 방문한다는 뜻
            while graph[x]:
                # 어휘 순 방문 -> 가장 첫 번째 값
                dfs(graph[x].pop(0))

            answer.append(x)

        dfs('JFK')

        answer.reverse()
        return answer
