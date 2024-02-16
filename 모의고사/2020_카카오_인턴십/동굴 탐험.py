import collections


def solution(n, path, order):
    graph = [[] for _ in range(n)]

    for n1, n2 in path:
        graph[n1].append(n2)
        graph[n2].append(n1)

    lock = {}
    key = {}
    for pre, nxt in order:
        lock[nxt] = pre
        key[pre] = nxt

    queue = collections.deque()
    queue.append(0)

    visited = set()
    visited_lock = set()

    while queue:
        cur = queue.popleft()
        if cur in lock:
            visited_lock.add(cur)
            continue

        visited.add(cur)
        if cur in key:
            if key[cur] in visited_lock:
                visited_lock.remove(key[cur])
                queue.append(key[cur])
            del lock[key[cur]]
            del key[cur]

        for i in graph[cur]:
            if i not in visited:
                queue.append(i)

    return len(visited) == n
