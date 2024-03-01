import collections


def solution(places):
    ans = []
    for place in places:
        board = [[-1] * 5 for _ in range(5)]
        p = []

        for y, row in enumerate(place):
            for x, ch in enumerate(row):
                if ch == 'P':
                    p.append((x, y))
                board[y][x] = ch

        ok = True
        for sx, sy in p:
            ok = ok & bfs(board, sx, sy, p)
        ans.append(1 if ok else 0)

    return ans


def bfs(board, sx, sy, p):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    dist = [[float('inf')] * 5 for _ in range(5)]

    dist[sy][sx] = 0
    queue = collections.deque([(sx, sy)])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < 5 and 0 <= ny < 5:
                if board[ny][nx] != 'X' and dist[ny][nx] == float('inf'):
                    dist[ny][nx] = dist[y][x] + 1
                    queue.append((nx, ny))

    for x, y in p:
        if sx == x and sy == y:
            continue
        if dist[y][x] <= 2:
            return False

    return True
