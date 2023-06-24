class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        dist = [-1] * n

        for start, end, cost in flights:
            graph[start].append((end, cost))

        queue = collections.deque([(src, 0, 0)])
        dist[src] = 0

        while queue:
            node, cost, count = queue.popleft()

            for next_node, edge_cost in graph[node]:
                if count <= k and (dist[next_node] == -1 or dist[next_node] > cost + edge_cost):
                    dist[next_node] = cost + edge_cost
                    queue.append((next_node, cost + edge_cost, count + 1))

        return dist[dst]
