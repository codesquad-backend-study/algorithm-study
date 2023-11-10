# 이전 방향과 다른 방향으로 움직인다면, 6칸 증가
# 이전 방향과 같은 방향으로 움직인다면, 1칸 증가
# 방향이 바뀌었음을 체크하기 위해, bfs 는 [x, x] 로 만들어야 할 듯?

import collections


def solution(board):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    NOT_VISIT = 1000_0000
    START = -1
    DOWN = 0
    UP = 1
    LEFT = 2
    RIGHT = 3

    w = len(board[0])
    h = len(board)
    dist = [[[NOT_VISIT] * 4 for _ in range(w)] for _ in range(h)]

    queue = collections.deque()
    queue.append((0, 0, START))
    dist[0][0][DOWN] = 0
    dist[0][0][UP] = 0
    dist[0][0][LEFT] = 0
    dist[0][0][RIGHT] = 0

    while queue:
        x, y, dir = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < w and 0 <= ny < h:
                if board[ny][nx] != 1:
                    if dir == START:
                        dist[ny][nx][i] = dist[y][x][i] + 1
                        queue.append((nx, ny, i))

                    if i == dir and dist[ny][nx][dir] > dist[y][x][dir] + 1:
                        dist[ny][nx][dir] = dist[y][x][dir] + 1
                        queue.append((nx, ny, dir))

                    if i != dir and dist[ny][nx][i] > dist[y][x][dir] + 6:
                        dist[ny][nx][i] = dist[y][x][dir] + 6
                        queue.append((nx, ny, i))

    return min(dist[-1][-1]) * 100
