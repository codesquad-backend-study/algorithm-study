from collections import deque


def solution(board):
    N = len(board)
    costs = [[[600 * N] * 4 for _ in range(N)] for _ in range(N)]
    costs[0][0] = [0, 0, 0, 0]

    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    # direction = ['right', 'left', 'down', 'up', 'none']
    queue = deque([(0, 0, 4, 0)])  # (r, c, direction, cost)

    while queue:
        r, c, d, cost = queue.popleft()

        for i in range(4):
            nr = dr[i] + r
            nc = dc[i] + c

            if 0 <= nr < N and 0 <= nc < N:
                plus = 1 if d == 4 or d == i else 6

                if not board[nr][nc] and costs[nr][nc][i] > cost + plus:
                    costs[nr][nc][i] = cost + plus
                    queue.append((nr, nc, i, cost + plus))

    return min(costs[-1][-1]) * 100


print(solution([[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [1, 0, 0, 0, 1], [1, 1, 1, 0, 0]]))
