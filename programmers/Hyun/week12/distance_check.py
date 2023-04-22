import collections


def solution(places):
    ans = []

    for each_board in places:
        board = []
        for line in each_board:
            board.append(list(line))
        ans.append(check(board))

    return ans


def check(board):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue = collections.deque()

    for sy in range(5):
        for sx in range(5):
            if board[sy][sx] != "P":
                continue

            visit = [[False] * 5 for _ in range(5)]

            queue.append((sx, sy, 0))
            visit[sy][sx] = True

            nearest = 100

            while queue:
                x, y, depth = queue.popleft()
                if board[y][x] == "P" and not (x == sx and y == sy):
                    nearest = min(depth, nearest)

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < 5 and 0 <= ny < 5:
                        if not visit[ny][nx]:
                            if board[y][x] == "X":
                                depth += 1
                            queue.append((nx, ny, depth + 1))
                            visit[ny][nx] = True

            if nearest < 3:
                return 0

    return 1
