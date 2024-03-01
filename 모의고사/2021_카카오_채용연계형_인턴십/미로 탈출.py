import collections
import heapq


def solution(n, start, end, roads, traps):
    traps = set(traps)

    graph = collections.defaultdict(list)
    for u, v, w in roads:
        graph[u].append((v, w, False))
        graph[v].append((u, w, True))

    flipped = [False] * (n + 1)
    heap = [(0, start, flipped)]

    start_state = (start, False, tuple([False] * len(graph[start])))
    dist = {}
    dist[start_state] = 0

    while heap:
        distance, current_node, flipped = heapq.heappop(heap)

        current_node_state = (current_node, flipped[current_node], tuple(flipped[next_node] for next_node, _, _ in graph[current_node]))
        if distance > dist.get(current_node_state, float('inf')):
            continue

        for next_node, cost, valid_when_flipped in graph[current_node]:
            edge_flipped = flipped[current_node] ^ flipped[next_node]

            if (valid_when_flipped is False and edge_flipped is False) or (valid_when_flipped is True and edge_flipped is True):

                f = flipped[:]
                if next_node in traps:
                    f[next_node] = not f[next_node]

                next_node_state = (next_node, f[next_node], tuple(flipped[n] for n, _, _ in graph[next_node]))

                if distance + cost < dist.get(next_node_state, float('inf')):
                    dist[next_node_state] = distance + cost
                    heapq.heappush(heap, (distance + cost, next_node, f))

    candidates = [dist[k] for k in dist if k[0] == end]
    return min(candidates)
