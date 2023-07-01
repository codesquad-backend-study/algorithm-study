import collections
import heapq
from typing import List


def networkDelayTime(times: List[List[int]], n: int, k: int):
    graph = collections.defaultdict(list)

    for u, v, w in times:  # 출발지, 도착지, 소요 시간
        graph[u].append((v, w))  # 출발지 : (도착지, 소요 시간)
    print(graph)

    # 시작 지점으로 세팅
    queue = [(0, k)]  # 소요 시간, 노드
    dictionary = collections.defaultdict(int)

    # 우선 순위 큐를 사용해서 해당 레벨에서 이동하는 데 걸리는 시간이 가장 짧은 것을 먼저 추출
    while queue:
        print("현재 큐 : ", queue)
        time, node = heapq.heappop(queue)
        print("popped time=", time, ", popped node=", node)
        if node not in dictionary:  # 방문한 적이 없는 노드인 경우 추가
            dictionary[node] = time
            print("현재 딕셔너리 : ", dictionary)
            for v, w in graph[node]:
                alt = time + w  # 현재 소요 시간에 다음 노드의 소요 시간을 추가한다
                print("현재 큐: ", queue)
                heapq.heappush(queue, (alt, v))

    print(len(dictionary))
    print(n)

    # 끊기지 않고 모든 노드를 방문했는지 확인
    if len(dictionary) == n:
        return max(dictionary.values())
    return -1


print(networkDelayTime(
    [[3, 1, 5], [3, 2, 2], [2, 1, 2], [3, 4, 1], [4, 5, 1], [5, 6, 1], [6, 7, 1], [7, 8, 1], [8, 1, 1]], 8, 3))
