def solution(info, edges):
    graph = [[] for _ in range(17)]

    for n1, n2 in edges:
        graph[n1].append(n2)

    global ans
    ans = 0

    def go(n, sheep, wolf, reachable):
        sheep += 1 - info[n]
        wolf += info[n]

        if sheep <= wolf:
            return

        reachable.remove(n)
        global ans
        ans = max(ans, sheep)

        for child_node in graph[n]:
            reachable.append(child_node)

        for next_node in reachable:
            go(next_node, sheep, wolf, reachable[:])

    go(0, 0, 0, [0])

    return ans
