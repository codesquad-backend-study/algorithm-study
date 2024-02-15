# 직선 도로 = 100 원, 코너 = 500원
# 경주로 최소 비용 반환
# 1은 벽, 0은 길
import collections


def solution(board):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    dist = [[[float('inf'), float('inf'), float('inf'), float('inf')] for _ in range(len(board))] for _ in range(len(board))]
    queue = collections.deque()
    queue.append((0, 0, 'start'))
    dist[0][0][0] = dist[0][0][1] = dist[0][0][2] = dist[0][0][3] = 0

    while queue:
        x, y, v = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < len(board) and 0 <= ny < len(board):
                if board[ny][nx] == 0:
                    if v == 'start':
                        dist[ny][nx][i] = 100
                        queue.append((nx, ny, i))
                    elif v == i and dist[ny][nx][i] > dist[y][x][v] + 100:
                        dist[ny][nx][i] = dist[y][x][i] + 100
                        queue.append((nx, ny, i))
                    elif v != i and dist[ny][nx][i] > dist[y][x][v] + 600:
                        dist[ny][nx][i] = dist[y][x][v] + 600
                        queue.append((nx, ny, i))

    return min(dist[-1][-1])
