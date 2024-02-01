import collections
from copy import deepcopy
from itertools import permutations


def move_cost(board, start, end):
    if start == end:
        return 0

    queue, visit = collections.deque([[start[0], start[1], 0]]), {start}
    while queue:
        x, y, c = queue.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy  # normal move
            cx, cy = x, y
            while True:  # Ctrl + move
                cx, cy = cx + dx, cy + dy
                if not (0 <= cx <= 3 and 0 <= cy <= 3):
                    cx, cy = cx - dx, cy - dy
                    break
                elif board[cx][cy] != 0:
                    break

            if (nx, ny) == end or (cx, cy) == end:
                return c + 1

            if (0 <= nx <= 3 and 0 <= ny <= 3) and (nx, ny) not in visit:
                queue.append((nx, ny, c + 1))
                visit.add((nx, ny))
            if (cx, cy) not in visit:
                queue.append((cx, cy, c + 1))
                visit.add((cx, cy))


def cls_cost(board, cdict, curr, order, cost):
    if len(order) == 0:
        return cost
    idx = order[0] + 1

    choice1 = move_cost(board, curr, cdict[idx][0]) + move_cost(board, cdict[idx][0], cdict[idx][1]) + 2
    choice2 = move_cost(board, curr, cdict[idx][1]) + move_cost(board, cdict[idx][1], cdict[idx][0]) + 2

    new_board = deepcopy(board)
    new_board[cdict[idx][0][0]][cdict[idx][0][1]] = 0
    new_board[cdict[idx][1][0]][cdict[idx][1][1]] = 0

    if choice1 < choice2:
        return cls_cost(new_board, cdict, cdict[idx][1], order[1:], cost + choice1)
    else:
        return cls_cost(new_board, cdict, cdict[idx][0], order[1:], cost + choice2)


def solution(board, r, c):
    answer = float('inf')
    cdict = collections.defaultdict(list)
    for row in range(4):
        for col in range(4):
            num = board[row][col]
            if num != 0:
                cdict[num].append((row, col))

    for case in permutations(range(len(cdict)), len(cdict)):
        answer = min(answer, cls_cost(board, cdict, (r, c), case, 0))

    return answer
