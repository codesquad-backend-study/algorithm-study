import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)

        for x, y in prerequisites:
            graph[x].append(y)

        traced, visited = set(), set()

        def dfs(index) -> bool:
            # 순환 구조일 때
            if index in traced:
                return False

            # 이미 방문했던 노드일 때
            if index in visited:
                return True

            traced.add(index)

            for y in graph[index]:
                # 순환 구조일 때
                if not dfs(y):
                    return False

            # 탐색 종료 후 -> 순환, 방문 노드 각각 삭제, 추가
            traced.remove(index)
            visited.add(index)

            return True

        for x in list(graph):
            if not dfs(x):
                return False

        return True
