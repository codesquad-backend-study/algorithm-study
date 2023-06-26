import collections
from typing import List


# 그래프가 순환 구조인지 판별하는 문제
# 이미 방문했던 곳을 중복 방문하게 된다면 순환 구조로 간주할 수 있다

def canFinish(numCourses: int, prerequisites: List[List[int]]):
    # 풀이 1
    # def dfs(i):
    #     print("i = ", i)
    #     print("traced = ", traced)
    #     if i in traced:
    #         return False  # 방문했던 곳이라면 False를 return
    #
    #     traced.add(i)  # 처음 방문한 경우 기록
    #     print("* add to traced = ", traced)
    #     for y in graph[i]:  # 이어서 계속 탐색
    #         print("y = ", y)
    #         if not dfs(y):
    #             return False
    #
    #     traced.remove(i)  # 방문했던 내역을 삭제
    #     print("방문한 내역을 삭제 : ", i)
    #
    #     return True
    #
    # graph = collections.defaultdict(list)
    # for x, y in prerequisites:
    #     graph[x].append(y)
    #
    # print("defaultdict graph = ", graph)
    # print("list graph = ", list(graph))
    # traced = set()
    #
    # for x in list(graph):
    #     print("x = ", x)
    #     if not dfs(x):  # 방문했던 곳이라면 False를 return
    #         return False  # 방문했던 곳을 또 방문헸기 때문에 순환 구조로 판단하고 최종적으로 False를 return
    #
    # print("True")
    # return True

    # 풀이 2
    graph = collections.defaultdict(list)
    for x, y in prerequisites:
        graph[x].append(y)

    print(graph)
    print()

    traced = set()
    visited = set()

    def dfs(i):
        # 순환 구조이면 False
        print("i = ", i)
        if i in traced:
            print("[T] 추적했던 노드 i = ", i)
            return False
        # 이미 방문했던 노드이면 True
        if i in visited:
            print("[V] 방문했던 노드 i = ", i)
            return True

        traced.add(i)
        print("+ traced에 추가한 노드 i = ", i)
        print("현재 traced: ", traced)
        for y in graph[i]:
            if not dfs(y):
                return False

        traced.remove(i)
        print("--- traced에서 제거할 노드 i = ", i)
        visited.add(i)
        print("* visited에 추가한 노드 i = ", i)
        print("현재 visted: ", visited)

        return True

    for x in list(graph):
        if not dfs(x):
            return False

    return True


canFinish(4, [[1, 0], [2, 1], [3, 2], [3, 1]])
