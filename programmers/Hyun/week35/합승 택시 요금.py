import collections


def solution(n, s, a, b, fares):
    NOT_VISIT = 10_0000 * 200 * 10

    graph = [[] for _ in range(n + 1)]

    for n1, n2, fare in fares:
        graph[n1].append((n2, fare))
        graph[n2].append((n1, fare))

    def bfs(start, end):
        dist = [NOT_VISIT] * (n + 1)

        queue = collections.deque()
        queue.append(start)
        dist[start] = 0

        while queue:
            cur = queue.popleft()
            for node, fare in graph[cur]:
                if dist[node] > dist[cur] + fare:
                    dist[node] = dist[cur] + fare
                    queue.append(node)

        return dist[end]

    def calculate_joint_cost():
        dist = [NOT_VISIT] * (n + 1)

        queue = collections.deque()
        queue.append(s)
        dist[s] = 0

        while queue:
            cur = queue.popleft()
            for node, fare in graph[cur]:
                if dist[node] > dist[cur] + fare:
                    dist[node] = dist[cur] + fare
                    queue.append(node)

        return dist

    def caculate_total_cost(joint_node):
        return bfs(joint_node, a) + bfs(joint_node, b) + joint_cost[joint_node]

    joint_cost = calculate_joint_cost()

    ans = NOT_VISIT
    for joint_node in range(1, n + 1):
        ans = min(ans, caculate_total_cost(joint_node))

    return ans
