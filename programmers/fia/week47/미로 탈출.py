from collections import defaultdict
from heapq import heappop, heappush


def solution(n, start, end, roads, traps):  # 미해결
    status = [0] * (n + 1)  # 0: 기존 방향  1: 뒤집힌 방향

    graph = defaultdict(list)
    for p, q, s in roads:
        graph[p].append((q, s, 0))

        if p in traps or q in traps:
            graph[q].append((p, s, 1))

    # [0, 0 상태일 때, 0, 1 상태일 때, 1, 0 상태일 때, 1, 1 상태일 때]
    visited = [[float("inf"), float("inf"), float("inf"), float("inf")] for _ in range(n + 1)]
    queue = []
    heappush(queue, (0, start, 0))  # (누적 비용, 현재 위치, 상태)

    while queue:
        cost, node, direction = heappop(queue)

        if visited[node][direction] < cost:
            continue

        visited[node][direction] = cost

        if node == end:
            continue

        if node in traps:
            status[node] = 1 if status[node] == 0 else 0

        for connection in graph[node]:
            destination, score, check = connection

            if status[node] and status[destination] and check == 0:  # 둘 다 활성화된 함정이라면 상쇄
                heappush(queue, (cost + score, destination, 3))  # 기존 방향대로 이동
            elif not status[node] and not status[destination] and check == 0:  # 둘 다 비활성화 상태라면
                heappush(queue, (cost + score, destination, 0))  # 기존 방향대로 이동
            elif status[node] and check == 1:  # 자신만 활성화된 함정이라면
                heappush(queue, (cost + score, destination, 2))  # 반대 방향으로 이동
            elif status[destination] and check == 1:  # 목적지만 활성화된 상태라면
                heappush(queue, (cost + score, destination, 1))  # 반대 방향으로 이동

    return min(visited[end])
