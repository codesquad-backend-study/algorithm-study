import collections


def can_move(cur1, cur2, new_board):
    x, y = 1, 0
    cand = []
    DELTAS = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    # 평행이동
    for dy, dx in DELTAS:
        nxt1 = (cur1[y] + dy, cur1[x] + dx)
        nxt2 = (cur2[y] + dy, cur2[x] + dx)
        if new_board[nxt1[y]][nxt1[x]] == 0 and new_board[nxt2[y]][nxt2[x]] == 0:
            cand.append((nxt1, nxt2))

    # 회전
    if cur1[y] == cur2[y]:  # 가로방향 -> 세로방향 회전
        UP, DOWN = -1, 1
        for d in [UP, DOWN]:
            if new_board[cur1[y] + d][cur1[x]] == 0 and new_board[cur2[y] + d][cur2[x]] == 0:
                cand.append((cur1, (cur1[y] + d, cur1[x])))
                cand.append((cur2, (cur2[y] + d, cur2[x])))

    else:  # 세로방향 -> 가로방향 회전
        LEFT, RIGHT = -1, 1
        for d in [LEFT, RIGHT]:
            if new_board[cur1[y]][cur1[x] + d] == 0 and new_board[cur2[y]][cur2[x] + d] == 0:
                cand.append(((cur1[y], cur1[x] + d), cur1))
                cand.append(((cur2[y], cur2[x] + d), cur2))
    return cand


def solution(board):
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]

    que = collections.deque([((1, 1), (1, 2), 0)])
    confirm = set([((1, 1), (1, 2))])

    while que:
        cur1, cur2, count = que.popleft()
        if cur1 == (n, n) or cur2 == (n, n):
            return count
        for nxt in can_move(cur1, cur2, new_board):
            if nxt not in confirm:
                que.append((*nxt, count + 1))
                confirm.add(nxt)
