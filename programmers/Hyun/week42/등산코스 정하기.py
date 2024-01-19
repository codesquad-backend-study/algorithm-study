import heapq


def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n + 1)]
    gates = set(gates)
    summits = set(summits)

    for n1, n2, w in paths:
        if n1 in gates:
            graph[n1].append((n2, w))
        elif n2 in gates:
            graph[n2].append((n1, w))
        elif n1 in summits:
            graph[n2].append((n1, w))
        elif n2 in summits:
            graph[n1].append((n2, w))
        else:
            graph[n1].append((n2, w))
            graph[n2].append((n1, w))

    def dijkstra(gates):
        intensity = [float('inf')] * (n + 1)

        heap = []
        for gate in gates:
            intensity[gate] = 0
            heapq.heappush(heap, (0, gate))

        while heap:
            weight, current = heapq.heappop(heap)
            if intensity[current] < weight:
                continue

            for v, w in graph[current]:
                current_intensity = max(weight, w)

                if intensity[v] > current_intensity:
                    intensity[v] = current_intensity
                    heapq.heappush(heap, (current_intensity, v))

        return intensity

    intensity = dijkstra(gates)

    min_summit = -1
    min_intensity = 2e9
    for summit in sorted(summits):
        if intensity[summit] < min_intensity:
            min_summit = summit
            min_intensity = intensity[summit]

    return [min_summit, min_intensity]


print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))
# [5, 3]

print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]))
# [3, 4]
