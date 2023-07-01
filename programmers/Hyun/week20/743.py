class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = [[] for _ in range(n + 1)]
        dist = [-1] * (n + 1)

        for start, end, weight in times:
            graph[start].append((end, weight))

        queue = collections.deque([(k, 0)])
        dist[k] = 0

        count = 0

        while queue:
            node, weight = queue.popleft()
            count += 1
            for next_node, edge_weight in graph[node]:
                if dist[next_node] == -1 or dist[next_node] > edge_weight + weight:
                    dist[next_node] = edge_weight + weight
                    queue.append((next_node, edge_weight + weight))

        if count < n:
            return -1
        return max(dist) if max(dist) != 0 else -1
