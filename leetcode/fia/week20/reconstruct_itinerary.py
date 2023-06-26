import collections
from typing import List


def findItinerary(tickets: List[List[str]]) -> List[str]:
    tickets.sort()
    graph = collections.defaultdict(collections.deque)
    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])

    # 풀이 1
    # route = []
    #
    # def dfs(location):
    #     while graph[location]:
    #         print("현재 그래프 : ", graph[location])
    #         print("pop한 노드: ", graph[location][0])
    #         dfs(graph[location].popleft())
    #     print("+ append할 노드: ", location)
    #     route.append(location)
    #     print("route : ", route)
    #
    # dfs("JFK")
    # print(route[::-1])

    # 풀이 2
    route, stack = [], ["JFK"]
    while stack:
        print(stack[-1], "의 그래프 확인 : ", graph[stack[-1]])
        while graph[stack[-1]]:
            print("스택에 들어갈 노드 : ", graph[stack[-1]][0])
            stack.append(graph[stack[-1]].popleft())
            print("* 현재 스택 확인 : ", stack)
        print("+ 루트에 들어갈 노드 : ", stack[-1])
        route.append(stack.pop())
        print("--- 현재 루트 확인 : ", route)

        print(route[::-1])
    return route[::-1]


findItinerary([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]])
