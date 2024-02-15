from collections import deque


def solution(n, path, order):  # 미해결
    route = [[] for _ in range(n)]
    visited = [False] * n

    for a, b in path:
        route[a].append(b)
        route[b].append(a)

    key = [0] * n
    lock = [0] * n

    for a, b in order:
        key[a] = b
        lock[b] = a

    queue = deque([0])
    revisits = set()

    while queue:
        room = queue.popleft()

        visited[room] = True

        if key[room] != 0:  # 자신이 key 방이라면 lock 방 열어주기
            lock[key[room]] = 0

        for other_room in route[room]:
            if not visited[other_room] and lock[other_room] == 0:
                queue.append(other_room)
            else:  # 잠겨있는 방이라면 재방문 표시 해두기
                revisits.add(other_room)

    return sum(visited) == n


print(solution(9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[8, 5], [6, 7], [4, 1]]))
print(solution(9, [[8, 1], [0, 1], [1, 2], [0, 7], [4, 7], [0, 3], [7, 5], [3, 6]], [[4, 1], [5, 2]]))
