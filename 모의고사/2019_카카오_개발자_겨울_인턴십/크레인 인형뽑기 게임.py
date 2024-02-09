import collections


def solution(board, moves):
    col_board = [collections.deque() for _ in range(len(board))]

    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x] != 0:
                col_board[x].appendleft(board[y][x])

    ans = 0
    basket = []
    for move in moves:
        idx = move - 1
        if not col_board[idx]:
            continue

        doll = col_board[idx].pop()

        if basket and basket[-1] == doll:
            ans += 2
            basket.pop()
        else:
            basket.append(doll)

    return ans
