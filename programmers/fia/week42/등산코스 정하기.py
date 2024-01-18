from collections import defaultdict
from heapq import heappop, heappush


def solution(n, paths, gates, summits):
    graph = defaultdict(list)

    for i, j, w in paths:
        graph[i].append((j, w))
        graph[j].append((i, w))

    summits_set = set(summits)
    intensities = [float('inf')] * (n + 1)
    heap = []

    for gate in gates:
        intensities[gate] = 0
        heappush(heap, (0, gate))

    while heap:
        i, n = heappop(heap)

        if intensities[n] < i or n in summits_set:
            continue

        for j, ji in graph[n]:
            ni = max(i, ji)

            if intensities[j] > ni:
                intensities[j] = ni
                heappush(heap, (ni, j))

    answer = [-1, float('inf')]

    for summit in sorted(summits):
        if answer[1] > intensities[summit]:
            answer = [summit, intensities[summit]]

    return answer
